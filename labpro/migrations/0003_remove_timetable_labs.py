# Generated by Django 5.0.4 on 2024-05-08 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("labpro", "0002_timetable_labs"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="timetable",
            name="labs",
        ),
    ]
