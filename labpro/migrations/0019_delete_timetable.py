# Generated by Django 5.0.4 on 2024-05-23 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("labpro", "0018_delete_timetableentry"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Timetable",
        ),
    ]
