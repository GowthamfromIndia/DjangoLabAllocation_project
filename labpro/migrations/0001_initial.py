# Generated by Django 5.0.4 on 2024-05-08 07:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Authentication", "0004_remove_department_institution"),
    ]

    operations = [
        migrations.CreateModel(
            name="Labs",
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
                ("lab_1", models.CharField(blank=True, max_length=100, null=True)),
                ("capacity_lab1", models.IntegerField(blank=True, null=True)),
                ("items_1", models.TextField(blank=True, max_length=1500)),
                ("lab_2", models.CharField(blank=True, max_length=100, null=True)),
                ("capacity_lab2", models.IntegerField(blank=True, null=True)),
                ("items_2", models.TextField(blank=True, max_length=1500)),
                ("lab_3", models.CharField(blank=True, max_length=100, null=True)),
                ("capacity_lab3", models.IntegerField(blank=True, null=True)),
                ("items_3", models.TextField(blank=True, max_length=1500)),
                ("lab_4", models.CharField(blank=True, max_length=100, null=True)),
                ("capacity_lab4", models.IntegerField(blank=True, null=True)),
                ("items_4", models.TextField(blank=True, max_length=1500)),
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
        migrations.CreateModel(
            name="Timetable",
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
