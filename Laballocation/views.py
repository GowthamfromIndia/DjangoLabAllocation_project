from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from .forms import ChangePasswordForm,ProfileForm,MessageForm,NotificationForm
from .models import Notifications,Message
from Authentication.models import Department,Profile
from labpro.models import Labs
import logging
from django.shortcuts import render,HttpResponseRedirect,reverse,redirect,get_object_or_404
from django.contrib import messages as django_messages
from django.utils import timezone
import random

logger = logging.getLogger(__name__)

@login_required
def services(request):
    return render(request, 'services.html')

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def contactus(request):
    return render(request, 'contactus.html')

@login_required
def Homepage(request):
    return render(request, 'Homepage.html', {'profile': request.user.profile})


@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    institution = profile.institution
    return render(request, 'profile.html', {'profile': profile, 'institution': institution})

@login_required
def edit_profile(request):
    form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user.profile, files=request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.is_new = False
            profile.save()
            return HttpResponseRedirect(reverse('Laballocation:profile'))
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def change_password(request):
    user = request.user
    form = ChangePasswordForm(user=user)
    if request.method == 'POST':
        form = ChangePasswordForm(user=user, data=request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data.get('new_password'))
            user.save()
            messages.success(request, 'Your password was updated successfully, please sign in using your new password.')
            return HttpResponseRedirect(reverse('')) 
    return render(request, 'change_password_form.html', {'form': form})



@login_required
def message(request):
    user_profile = request.user.profile
    institution = user_profile.institution
    user_department = user_profile.department
    messages = Message.objects.filter(institution=institution, department=user_department)

    if request.user.is_superuser:
        if request.method == 'POST':
            if 'delete_message' in request.POST:
                message_id = request.POST.get('delete_message')
                try:
                    message = Message.objects.get(id=message_id, institution=institution, department=user_department)
                    message.delete()
                    django_messages.success(request, 'Message deleted successfully!')
                except Message.DoesNotExist:
                    django_messages.error(request, 'Message not found or you do not have permission to delete it.')
                return redirect('Laballocation:message')
            else:
                form = MessageForm(request.POST, user=request.user)
                if form.is_valid():
                    form.save()
                    django_messages.success(request, 'Message added successfully!')
                    return redirect('Laballocation:message')
                else:
                    django_messages.error(request, 'Failed to add message. Please correct the errors.')
        else:
            form = MessageForm(user=request.user)
        return render(request, 'message.html', {'messages': messages, 'form': form})

    return render(request, 'message.html', {'messages': messages})




@login_required
def your_department(request):
    user_profile = request.user.profile
    user_department = user_profile.department
    institution = user_profile.institution
    students = Profile.objects.filter(department=user_department, institution=institution)
    #print("Department:", user_department)
    #print("Institution:", institution)
    #print("Students:", students)
    return render(request, 'your_department.html', {'students': students, 'institution': institution, 'department': user_department})

@login_required
def Notifications1(request):
    user_institution = request.user.profile.institution
    notifications = Notifications.objects.filter(institution=user_institution)

    if request.user.is_superuser:
        if request.method == 'POST':
            if 'add_notification' in request.POST:
                form = NotificationForm(request.POST)
                if form.is_valid():
                    notification = form.save(commit=False)
                    notification.institution = user_institution
                    notification.save()
                    return redirect('Laballocation:Notifications1')
            elif 'delete_notification' in request.POST:
                notification_id = request.POST.get('notification_id')
                Notifications.objects.filter(id=notification_id).delete()
                return redirect('Laballocation:Notifications1')
        else:
            form = NotificationForm()
    else:
        form = None

    return render(request, 'Notifications.html', {'notifications': notifications, 'form': form})

