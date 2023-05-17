# Generated by Django 3.2.17 on 2023-05-17 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0028_achivements_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achivements',
            name='year',
            field=models.CharField(choices=[('2020-21', '2020-21'), ('2021-22', '2021-22'), ('2022-23', '2022-23')], default='2022-23', max_length=200),
        ),
    ]
