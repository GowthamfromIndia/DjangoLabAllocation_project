# Generated by Django 5.0.4 on 2024-05-06 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Laballocation", "0030_timetable_department_timetable_end_time_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="timetable",
            name="day",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="end_time",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="start_time",
        ),
        migrations.AddField(
            model_name="timetable",
            name="labs",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Laballocation.labs",
            ),
        ),
    ]
