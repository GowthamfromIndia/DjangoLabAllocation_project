from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'Laballocation'

urlpatterns = [
    path('Homepage', views.Homepage, name='Homepage'),
    path('profile/', views.profile, name='profile'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contactus, name='contactus'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('message/', views.message, name='message'),
    path('Notifications1/', views.Notifications1, name='Notifications1'),
    path('your_department/', views.your_department, name='your_department'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)