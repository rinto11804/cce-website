# Generated by Django 3.2.23 on 2023-12-02 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0017_internalauditabout'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disciplinarycommittee',
            options={'verbose_name': 'Disciplinary Committee Member', 'verbose_name_plural': 'Disciplinary Committee Members'},
        ),
        migrations.AlterModelOptions(
            name='grivenceuser',
            options={'verbose_name': 'Grievance User', 'verbose_name_plural': 'Grievance Users'},
        ),
        migrations.AlterModelOptions(
            name='iqacmeetingminutes',
            options={'verbose_name': 'IQAC Meeting Minute', 'verbose_name_plural': 'IQAC Meeting Minutes'},
        ),
        migrations.AlterField(
            model_name='grievancebody',
            name='type',
            field=models.CharField(max_length=30),
        ),
    ]
