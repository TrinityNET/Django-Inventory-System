# Generated by Django 5.0.4 on 2024-04-29 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0009_alter_reservation_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='start_date',
            field=models.DateField(),
        ),
    ]