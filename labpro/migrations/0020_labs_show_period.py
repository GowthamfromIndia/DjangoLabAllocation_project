# Generated by Django 5.0.4 on 2024-05-24 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("labpro", "0019_delete_timetable"),
    ]

    operations = [
        migrations.AddField(
            model_name="labs_show",
            name="period",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
