from django import forms
from .models import Profile,Message,Notifications
import re

PW_NAME_ERROR = 'Password must not include any part of your name.'
PW_CASING_ERROR = 'Password needs at least one {} letter.'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MessageForm, self).__init__(*args, **kwargs)
        if user:
            self.user = user

    def save(self, commit=True):
        instance = super(MessageForm, self).save(commit=False)
        instance.institution = self.user.profile.institution
        instance.department = self.user.profile.department
        if commit:
            instance.save()
        return instance


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'avatar', 'bio', 'date_of_birth', 'email']

    confirm_email = forms.EmailField(required=False)
    date_of_birth = forms.DateField(
        required=False,
        widget = forms.DateInput(format='%m/%d/%Y'),
        input_formats=('%m/%d/%Y', '%m/%d/%y', '%Y-%m-%d')
    )

    def clean_bio(self):
        data = self.cleaned_data.get('bio', None)
        if data and len(data) < 10:
            raise forms.ValidationError('Bio must be at least 10 characters.')
        return data

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email', None)
        confirm_email = cleaned_data.get('confirm_email', None)
        if email is not None or confirm_email is not None:
            if email != confirm_email:
                raise forms.ValidationError('Emails must match!')


def validate_pw_length(value):
    if len(value) < 10:
        raise forms.ValidationError('New password must be at least 10 characters.')


def no_username(value, username):
    if username.lower() in value.lower():
        raise forms.ValidationError('Password must not include your username.')


def no_first_name(value, first_name):
    if first_name.lower() in value.lower():
        raise forms.ValidationError(PW_NAME_ERROR)


def no_last_name(value, last_name):
    if last_name.lower() in value.lower():
        raise forms.ValidationError(PW_NAME_ERROR)


def has_lowercase(value):
    result = re.search(r'[a-z]', value)
    if result is None:
        raise forms.ValidationError(PW_CASING_ERROR.format('lowercase'))


def has_uppercase(value):
    result = re.search(r'[A-Z]', value)
    if result is None:
        raise forms.ValidationError(PW_CASING_ERROR.format('uppercase'))


def has_numbers(value):
    result = re.search(r'[\d]', value)
    if result is None:
        raise forms.ValidationError('Password needs at least one number.')


def has_special_characters(value):
    result = re.search(r'[@!$#*]', value)
    if result is None:
        raise forms.ValidationError('Password must have at least one of the following characters: @ ! $ # *')


class ChangePasswordForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    current_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean_new_password(self):
        new_pw = self.cleaned_data['new_password']
        username = self.user.get_username()
        first_name = self.user.profile.first_name
        last_name = self.user.profile.last_name
        validate_pw_length(new_pw)
        no_username(new_pw, username)
        no_first_name(new_pw, first_name)
        no_last_name(new_pw, last_name)
        has_lowercase(new_pw)
        has_uppercase(new_pw)
        has_numbers(new_pw)
        has_special_characters(new_pw)
        return new_pw
        
    def clean(self):
        cleaned_data = super().clean()
        current_password = cleaned_data.get('current_password', '')
        new_password = cleaned_data.get('new_password', '')
        confirm_password = cleaned_data.get('confirm_password', '')

        if new_password and (new_password != confirm_password):
            raise forms.ValidationError('Passwords don\'t match! Please make sure you confirm your new password.')
        
        if new_password and (current_password == new_password):
            raise forms.ValidationError('Your new password can\'t be the same as your old password!')


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = ['content']
