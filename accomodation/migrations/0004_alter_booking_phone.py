# Generated by Django 5.0.3 on 2024-04-04 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accomodation', '0003_booking_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.IntegerField(),
        ),
    ]