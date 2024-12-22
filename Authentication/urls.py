from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'Authentication'

urlpatterns = [
    path('', views.Institution_view, name='Institution_view'),
    path('login/', views.login_user, name='login'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout_user')
    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
