from django import forms
from .models import Labs_show,Feedback,Labs
from .models import PracticalTimetable
from .models import Assignment
from django.contrib.auth.models import User

class AssignmentForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.none(), widget=forms.CheckboxSelectMultiple, required=False)
    
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'file', 'users']
    
    def __init__(self, *args, **kwargs):
        institution = kwargs.pop('institution', None)
        department = kwargs.pop('department', None)
        super().__init__(*args, **kwargs)
        if institution and department:
            self.fields['users'].queryset = User.objects.filter(profile__institution=institution, profile__department=department)




class PracticalTimetableForm(forms.ModelForm):
    class Meta:
        model = PracticalTimetable
        fields = ['practical', 'capacity', 'date', 'time_slot', 'start_time', 'end_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }



class LabsShowForm(forms.ModelForm):
    PERIOD_CHOICES = [
        ('Period 1', 'Period 1'),
        ('Period 2', 'Period 2'),
        ('Period 3', 'Period 3'),
        ('Period 4', 'Period 4'),
        ('Period 5', 'Period 5'),
        ('Period 6', 'Period 6'),
    ]

    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]

    period = forms.ChoiceField(choices=PERIOD_CHOICES)
    day = forms.ChoiceField(choices=DAY_CHOICES)
    start_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), required=False)
    end_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), required=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(LabsShowForm, self).__init__(*args, **kwargs)
        
        if self.user and self.user.is_superuser:
            self.fields['department'].queryset = self.fields['department'].queryset.filter(pk=self.user.profile.department.pk)
        else:
            self.fields['department'].queryset = self.fields['department'].queryset.none()

    def clean(self):
        cleaned_data = super().clean()
        labs = cleaned_data.get("labs")
        period = cleaned_data.get("period")
        day = cleaned_data.get("day")
        department = cleaned_data.get("department")
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        if start_time and end_time and start_time >= end_time:
            self.add_error('end_time', "End time must be after start time.")

        instance = self.instance
        if instance and instance.id:
            existing_labs = Labs_show.objects.exclude(id=instance.id)
        else:
            existing_labs = Labs_show.objects.none()

        if existing_labs.filter(period=period, day=day, institution=self.user.profile.institution, department=department).exists():
            self.add_error('period', "A lab already exists in the specified period on this day.")
        
        return cleaned_data

    class Meta:
        model = Labs_show
        fields = ['labs', 'capacity', 'items', 'department', 'period', 'day', 'start_time', 'end_time']



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
