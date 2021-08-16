# Generated by Django 3.2.4 on 2021-08-14 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_planner', models.CharField(max_length=20)),
                ('event_agenda', models.CharField(max_length=13)),
                ('event_duration', models.DateTimeField()),
                ('event_venue', models.CharField(max_length=10)),
                ('event_attendees', models.CharField(max_length=16)),
            ],
        ),
    ]
