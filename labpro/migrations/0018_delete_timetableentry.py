# Generated by Django 5.0.4 on 2024-05-22 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("labpro", "0017_rename_name_labs_labs_rename_name_labs_show_labs"),
    ]

    operations = [
        migrations.DeleteModel(
            name="TimetableEntry",
        ),
    ]
