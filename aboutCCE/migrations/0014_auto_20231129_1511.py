# Generated by Django 3.2.17 on 2023-11-29 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutCCE', '0013_committee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resulttable',
            name='api',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='resulttable',
            name='batch',
            field=models.CharField(max_length=100),
        ),
    ]
