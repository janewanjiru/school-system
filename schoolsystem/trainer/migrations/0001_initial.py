# Generated by Django 3.2.4 on 2021-08-14 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=12)),
                ('id_number', models.CharField(max_length=12)),
                ('salary', models.PositiveBigIntegerField()),
                ('job_tittle', models.CharField(max_length=20)),
                ('Photo', models.ImageField(upload_to='')),
                ('Email', models.EmailField(max_length=254)),
                ('Resume', models.FileField(upload_to='')),
                ('Days', models.CharField(max_length=7)),
            ],
        ),
    ]
