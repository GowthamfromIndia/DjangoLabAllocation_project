from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Institution, Profile

class RegisterForm(UserCreationForm):
    institution = forms.ModelChoiceField(queryset=Institution.objects.all(), required=True, help_text="Select your institution")

    class Meta:
        model = User
        fields = ['username', 'email', 'institution', 'password1', 'password2']
