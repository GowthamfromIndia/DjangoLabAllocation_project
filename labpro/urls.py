from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'labpro'

urlpatterns = [
    path('lab_allocation/', views.labs_view, name='labs_view'),
    path('Assignassignment/', views.Assignassignment, name='Assignassignment'),
    path('Practicals/', views.Practicals, name='Practicals'),
    path('delete_practical/<int:id>/', views.delete_practical, name='delete_practical'),
    path('feedback/', views.feedback, name='feedback'),
    path('labs/', views.labs, name='labs'),
    path('labs/edit/<int:lab_id>/', views.edit_lab, name='edit_lab'),
]
