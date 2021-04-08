# Generated by Django 3.1.7 on 2021-04-05 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genie', '0008_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parkingspot',
            name='renter',
        ),
        migrations.CreateModel(
            name='Rentals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('event', models.ManyToManyField(related_name='bookedEvent', to='genie.Event')),
                ('renter', models.ManyToManyField(related_name='currentRenter', to='genie.User')),
                ('spot', models.ManyToManyField(related_name='spot', to='genie.ParkingSpot')),
            ],
        ),
    ]
