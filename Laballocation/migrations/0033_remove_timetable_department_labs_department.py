# Generated by Django 5.0.4 on 2024-05-07 15:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Authentication", "0004_remove_department_institution"),
        (
            "Laballocation",
            "0032_remove_timetable_labs_timetable_capacity_lab1_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="timetable",
            name="department",
        ),
        migrations.AddField(
            model_name="labs",
            name="department",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Authentication.department",
            ),
        ),
    ]
