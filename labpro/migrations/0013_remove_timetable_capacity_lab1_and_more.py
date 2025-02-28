# Generated by Django 5.0.4 on 2024-05-20 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Authentication", "0004_remove_department_institution"),
        ("labpro", "0012_rename_capacity_lab1_labs_capacity_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="timetable",
            name="capacity_lab1",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="capacity_lab2",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="capacity_lab3",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="capacity_lab4",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="capacity_lab5",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="end_time_1",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="end_time_2",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="end_time_3",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="end_time_4",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="end_time_5",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="items_1",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="items_2",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="items_3",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="items_4",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="items_5",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="lab_1",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="lab_2",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="lab_3",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="lab_4",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="lab_5",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="start_time_1",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="start_time_2",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="start_time_3",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="start_time_4",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="start_time_5",
        ),
        migrations.AddField(
            model_name="timetable",
            name="day_of_week",
            field=models.CharField(default=True, max_length=10),
        ),
        migrations.AddField(
            model_name="timetable",
            name="end_time",
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name="timetable",
            name="lab",
            field=models.ForeignKey(
                default=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="labpro.labs",
            ),
        ),
        migrations.AddField(
            model_name="timetable",
            name="start_time",
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name="timetable",
            name="department",
            field=models.ForeignKey(
                default=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Authentication.department",
            ),
        ),
        migrations.AlterField(
            model_name="timetable",
            name="institution",
            field=models.ForeignKey(
                default=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Authentication.institution",
            ),
        ),
    ]
