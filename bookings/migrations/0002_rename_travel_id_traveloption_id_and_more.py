# Generated by Django 5.1.7 on 2025-03-14 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='traveloption',
            old_name='travel_id',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='traveloption',
            name='available_seats',
            field=models.IntegerField(),
        ),
    ]
