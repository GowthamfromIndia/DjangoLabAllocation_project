from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


class Institution(models.Model):
    Iname = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Iname


class Department(models.Model):
    department = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.department


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    is_new = models.BooleanField(default=True)
    bio = models.TextField(max_length=1500, help_text='Tell us a bit about yourself.', blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    date_of_birth = models.DateField(
            null=True,
            blank=True,
            help_text='Please use one of the following formats: YYYY-MM-DD, MM/DD/YYYY, MM/DD/YY'
    )
    avatar = models.ImageField(
        blank=True,
        null=True,
        upload_to='avatars'
    )

    def __str__ (self):
        return f"{self.first_name} {self.last_name} 's profile"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'profile'):
        Profile.objects.create(user=instance)

