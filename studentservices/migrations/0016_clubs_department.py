# Generated by Django 3.2.17 on 2023-11-27 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentservices', '0015_clubsheroimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubs',
            name='department',
            field=models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('ME', 'ME'), ('CE', 'CE'), ('BSH', 'BSH'), ('None', 'None')], default='None', max_length=200),
        ),
    ]
