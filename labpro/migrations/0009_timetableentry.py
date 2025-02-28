# Generated by Django 5.0.4 on 2024-05-17 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("labpro", "0008_rename_feedback_feedback1"),
    ]

    operations = [
        migrations.CreateModel(
            name="TimetableEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_time", models.TimeField(blank=True, null=True)),
                ("end_time", models.TimeField(blank=True, null=True)),
                (
                    "lab",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="labpro.labs"
                    ),
                ),
                (
                    "timetable",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="entries",
                        to="labpro.timetable",
                    ),
                ),
            ],
        ),
    ]
