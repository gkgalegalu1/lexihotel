# Generated by Django 5.0.3 on 2024-04-01 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=9)),
                ('arrival_date', models.DateField()),
                ('leaving_date', models.DateField()),
                ('number_of_rooms', models.IntegerField()),
                ('number_of_adults', models.IntegerField()),
                ('number_of_kids', models.IntegerField()),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]
