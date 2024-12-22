from django.db import models
from django.contrib.auth.models import User
from Authentication.models import Institution, Department


class Labs(models.Model):
    labs = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.labs} Lab"

        

class Labs_show(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]

    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    labs = models.ForeignKey(Labs, on_delete=models.CASCADE, null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    items = models.TextField(max_length=1500, blank=True)
    period = models.CharField(max_length=20, null=True, blank=True)
    day = models.CharField(max_length=20, choices=DAYS_OF_WEEK, null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.institution} - {self.labs} ({self.period}) on {self.day}"



class PracticalTimetable(models.Model):
    TIME_SLOTS = [
        ('Forenoon', 'Forenoon'),
        ('Afternoon', 'Afternoon'),
    ]

    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    practical = models.CharField(max_length=255)
    capacity = models.IntegerField()
    date = models.DateField(null=True, blank=True)
    time_slot = models.CharField(max_length=20, choices=TIME_SLOTS)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.practical} - {self.time_slot} on {self.date}"



class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username}"


class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='assignments/', null=True, blank=True)

    def __str__(self):
        return self.title