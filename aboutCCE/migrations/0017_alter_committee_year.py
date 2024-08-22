# Generated by Django 3.2.23 on 2024-03-04 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutCCE', '0016_auto_20231130_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committee',
            name='year',
            field=models.CharField(choices=[('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024'), ('2024-2025', '2024-2025')], default=('2023-2024', '2023-2024'), max_length=200),
        ),
    ]
