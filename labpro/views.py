from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import render, HttpResponseRedirect,reverse,redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Labs,Feedback,Labs_show,Assignment,PracticalTimetable
from Authentication.models import Department,Profile,Institution
from .forms import LabsShowForm,FeedbackForm,AssignmentForm,PracticalTimetableForm
from django.contrib import messages
from django.db.models import Q


def is_admin(user):
    return user.is_superuser


@login_required
def Assignassignment(request):
    user_profile = request.user.profile
    user_institution = user_profile.institution
    user_department = user_profile.department

    if request.user.is_superuser:
        if request.method == 'POST':
            form = AssignmentForm(request.POST, request.FILES, institution=user_institution, department=user_department)
            if form.is_valid():
                assignment = form.save(commit=False)
                assignment.institution = user_institution
                assignment.department = user_department
                assignment.created_by = request.user
                assignment.save()
                form.save_m2m()  
                users = form.cleaned_data.get('users')
                assignment.users.set(users)
                messages.success(request, 'Assignment added and assigned successfully!')
                return redirect('labpro:Assignassignment')
            else:
                messages.error(request, 'Failed to add assignment. Please correct the errors.')
        else:
            form = AssignmentForm(institution=user_institution, department=user_department)

        assignments = Assignment.objects.filter(institution=user_institution, department=user_department)
        context = {
            'form': form,
            'assignments': assignments,
        }
    else:
        assignments = Assignment.objects.filter(institution=user_institution, department=user_department)
        context = {
            'assignments': assignments,
        }

    return render(request, 'Assignassignment.html', context)




@login_required
def labs_view(request):
    user_profile = request.user.profile
    user_department = user_profile.department
    user_institution = user_profile.institution

    if request.user.is_superuser and request.user.profile.department == user_department:
        labs = Labs_show.objects.filter(institution=user_institution, department=user_department)

        if request.method == 'POST':
            if 'delete_lab' in request.POST:
                lab_id = request.POST.get('delete_lab')
                try:
                    lab_to_delete = Labs_show.objects.get(id=lab_id)
                    lab_to_delete.delete()
                    messages.success(request, 'Lab deleted successfully!')
                except Labs_show.DoesNotExist:
                    messages.error(request, 'Lab not found.')
                return redirect('labpro:labs_view')

            form = LabsShowForm(request.POST, user=request.user)
            if form.is_valid():
                lab = form.save(commit=False)
                lab.department = user_department
                lab.institution = user_institution
                lab.save()
                messages.success(request, 'Lab added successfully!')
                return redirect('labpro:labs_view')
            else:
                messages.error(request, 'Failed to add lab. Please correct the errors.')
        else:
            form = LabsShowForm(user=request.user)

        context = {
            'labs': labs,
            'form': form,
            'user_institution': user_institution,
        }
    else:
        allocated_labs = Labs_show.objects.filter(department=user_department, institution=user_institution)
        context = {
            'labs': allocated_labs,
            'user_institution': user_institution,
        }

    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    timetable = []
    for day in days_of_week:
        day_schedule = {'day': day, 'periods': []}
        for period in ['Period 1', 'Period 2', 'Period 3', 'Period 4', 'Period 5', 'Period 6']:
            lab = Labs_show.objects.filter(institution=user_institution, department=user_department, period=period, day=day).first()
            if lab:
                day_schedule['periods'].append({
                    'period': period,
                    'start_time': lab.start_time.strftime('%I:%M %p') if lab.start_time else '',
                    'end_time': lab.end_time.strftime('%I:%M %p') if lab.end_time else '',
                    'lab_name': lab.labs.labs,
                    'capacity': lab.capacity,
                    'lab_id': lab.id,
                })
            else:
                day_schedule['periods'].append({
                    'period': period,
                    'start_time': '',
                    'end_time': '',
                    'lab_name': 'Not Allocated',
                    'capacity': 'N/A',
                    'lab_id': None,
                })
        timetable.append(day_schedule)

    context['timetable'] = timetable

    return render(request, 'lab_allocation.html', context)


@login_required
def edit_lab(request, lab_id):
    lab = get_object_or_404(Labs_show, id=lab_id)
    
    if request.method == 'POST':
        form = LabsShowForm(request.POST, instance=lab, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lab updated successfully!')
            return redirect('labpro:labs_view')
        else:
            messages.error(request, 'Failed to update lab. Please correct the errors.')
    else:
        form = LabsShowForm(instance=lab, user=request.user)

    context = {
        'form': form,
        'lab_id': lab_id,
    }

    return render(request, 'edit_lab.html', context)




@login_required
def Assignassignment(request):
    return render(request, 'Assignassignment.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PracticalTimetableForm
from .models import PracticalTimetable

@login_required
def Practicals(request):
    user_profile = request.user.profile
    user_institution = user_profile.institution
    user_department = user_profile.department

    if request.user.is_superuser:
        if request.method == 'POST':
            form = PracticalTimetableForm(request.POST)
            if form.is_valid():
                practical_timetable = form.save(commit=False)
                practical_timetable.institution = user_institution
                practical_timetable.department = user_department
                practical_timetable.save()
                messages.success(request, 'Practical timetable added successfully!')
                return redirect('labpro:Practicals')
            else:
                messages.error(request, 'Failed to add practical timetable. Please correct the errors.')
        else:
            form = PracticalTimetableForm()

        timetables = PracticalTimetable.objects.filter(institution=user_institution, department=user_department)
        context = {
            'form': form,
            'timetables': timetables,
        }
    else:
        timetables = PracticalTimetable.objects.filter(institution=user_institution, department=user_department)
        context = {
            'timetables': timetables,
        }

    return render(request, 'Practicals.html', context)

@login_required
def delete_practical(request, id):
    if request.user.is_superuser:
        try:
            timetable = PracticalTimetable.objects.get(id=id)
            timetable.delete()
            messages.success(request, 'Practical timetable deleted successfully!')
        except PracticalTimetable.DoesNotExist:
            messages.error(request, 'Practical timetable not found.')
    return redirect('labpro:Practicals')


@login_required
def labs(request):
    return render(request,'labs.html')


@login_required
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            messages.success(request, 'Feedback submitted successfully!')
            return HttpResponseRedirect(reverse('labpro:feedback'))
    else:
        form = FeedbackForm()

    return render(request, 'feedback1.html', {'form': form})