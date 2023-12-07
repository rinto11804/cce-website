# Generated by Django 3.2.23 on 2023-12-07 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentservices', '0016_clubs_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='CCEVRAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CCEVREvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='CCEVR/events')),
            ],
        ),
        migrations.CreateModel(
            name='CCEVRTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('priority', models.IntegerField()),
                ('image', models.ImageField(upload_to='CCEVR/members')),
            ],
        ),
    ]
