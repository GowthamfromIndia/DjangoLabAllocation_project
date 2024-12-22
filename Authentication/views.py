from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout 
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Institution,Profile
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from .forms import RegisterForm


NEW_PASSWORD_RULES = [
    'Must be at least 8 characters long',
    'Must contain both lower and upper case letters',
    'Must contain at least one number',
    'Cannot contain the user\'s first or last name',
    'Cannot contain the username associated with the account',
    'Must contain one of the following characters: @ ! $ # *'
]

def Institution_view(request):
    if request.method == 'POST':
        institution_name = request.POST.get('Institutionname')
        request.session['Institutionname'] = institution_name
        try:
            Institution.objects.get(Iname=institution_name)
        except ObjectDoesNotExist:
            return render(request, 'Institution.html', {'error_message': 'Name of the Institution not Registered'})
        else:
            return redirect('Authentication:login')
    else:
        return render(request, 'Institution.html')


def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    if not user.is_superuser:
                        institution_name = request.session.get('Institutionname')
                        try:
                            institution = Institution.objects.get(Iname=institution_name)
                        except ObjectDoesNotExist:
                            messages.error(request, 'Invalid institution selected.')
                            return redirect('Authentication:Institution_view')

                        try:
                            profile = Profile.objects.get(user=user)
                        except Profile.DoesNotExist:
                            messages.error(request, 'Profile does not exist.')
                            return redirect('Authentication:Institution_view')

                        if profile.institution == institution:
                            login(request, user)
                            return redirect('Laballocation:Homepage')
                        else:
                            messages.error(request, 'Selected institution does not match user institution.')
                    else:
                        messages.error(request, 'Staff are not allowed to log in here.')
                else:
                    messages.error(request, 'That user account has been disabled.')
            else:
                messages.error(request, 'Username or password is incorrect.')
    return render(request, 'login.html', {'form': form})


def adminlogin(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    if user.is_superuser:
                        institution_name = request.session.get('Institutionname')
                        try:
                            institution = Institution.objects.get(Iname=institution_name)
                        except ObjectDoesNotExist:
                            messages.error(request, 'Invalid institution selected.')
                            return redirect('Authentication:Institution_view')

                        try:
                            profile = Profile.objects.get(user=user)
                        except Profile.DoesNotExist:
                            messages.error(request, 'Profile does not exist.')
                            return redirect('Authentication:Institution_view')

                        if profile.institution == institution:
                            login(request, user)
                            return redirect('Laballocation:Homepage')
                        else:
                            messages.error(request, 'Selected institution does not match user institution.')
                    else:
                        messages.error(request, 'You are not a staff member.')
                else:
                    messages.error(request, 'That user account has been disabled.')
            else:
                messages.error(request, 'Username or password is incorrect.')
                
    return render(request, 'adminlogin.html', {'form': form})



def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken. Please choose a different one.')
                return redirect('Authenticationregister')
            else:
                user = form.save()
                institution = form.cleaned_data.get('institution')
                Profile.objects.create(user=user, institution=institution)
                login(request, user)
                messages.success(request, 'Registration successful.')
                return redirect('Laballocation:Homepage')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



def logout_user(request):
    auth_logout(request)
    messages.success(request, 'You\'ve been signed out! Come back soon.')
    return redirect('Authentication:Institution_view')