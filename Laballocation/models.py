from django.db import models
from django.utils import timezone
from Authentication.models import Institution,Department,Profile

class Notifications(models.Model):
    content = models.TextField(max_length=1500, blank=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content[:50]

class Message(models.Model):
    content = models.TextField(max_length=1000, blank=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content[:50]


