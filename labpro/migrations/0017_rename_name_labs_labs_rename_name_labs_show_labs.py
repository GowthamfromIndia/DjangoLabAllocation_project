# Generated by Django 5.0.4 on 2024-05-20 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("labpro", "0016_remove_labs_capacity_remove_labs_department_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="labs",
            old_name="name",
            new_name="labs",
        ),
        migrations.RenameField(
            model_name="labs_show",
            old_name="name",
            new_name="labs",
        ),
    ]
