# Generated by Django 5.0.4 on 2024-04-29 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0006_equipment_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='onsite',
            field=models.BooleanField(default=False),
        ),
    ]
