# Generated by Django 5.0.4 on 2024-05-01 06:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Laballocation', '0005_remove_equipments_items_remove_equipments_lab'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipments',
            name='items_1',
            field=models.TextField(blank=True, max_length=1500),
        ),
        migrations.AddField(
            model_name='equipments',
            name='items_2',
            field=models.TextField(blank=True, max_length=1500),
        ),
        migrations.AddField(
            model_name='equipments',
            name='items_3',
            field=models.TextField(blank=True, max_length=1500),
        ),
        migrations.AddField(
            model_name='equipments',
            name='items_4',
            field=models.TextField(blank=True, max_length=1500),
        ),
        migrations.AddField(
            model_name='equipments',
            name='lab_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lab_1', to='Laballocation.labs'),
        ),
        migrations.AddField(
            model_name='equipments',
            name='lab_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lab_2', to='Laballocation.labs'),
        ),
        migrations.AddField(
            model_name='equipments',
            name='lab_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lab_3', to='Laballocation.labs'),
        ),
        migrations.AddField(
            model_name='equipments',
            name='lab_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lab_4', to='Laballocation.labs'),
        ),
    ]
