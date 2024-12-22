# Generated by Django 5.0.6 on 2024-05-27 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Authentication", "0004_remove_department_institution"),
        ("labpro", "0022_labs_show_end_time_labs_show_start_time_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PracticalTimetable",
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
                ("practical", models.CharField(max_length=255)),
                ("capacity", models.IntegerField()),
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("Monday", "Monday"),
                            ("Tuesday", "Tuesday"),
                            ("Wednesday", "Wednesday"),
                            ("Thursday", "Thursday"),
                            ("Friday", "Friday"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "time_slot",
                    models.CharField(
                        choices=[("Forenoon", "Forenoon"), ("Afternoon", "Afternoon")],
                        max_length=20,
                    ),
                ),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                (
                    "department",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Authentication.department",
                    ),
                ),
                (
                    "institution",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Authentication.institution",
                    ),
                ),
            ],
        ),
    ]
