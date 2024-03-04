# Generated by Django 3.2.23 on 2024-03-04 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0030_auto_20231209_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Techletics24',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='techletics24')),
                ('dept', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('ME', 'ME'), ('CE', 'CE'), ('BSH', 'BSH'), ('None', 'None')], max_length=100)),
            ],
            options={
                'verbose_name': 'Techletics 24 Image',
                'verbose_name_plural': 'Tecletics Images',
            },
        ),
        migrations.AlterField(
            model_name='admissiongraph',
            name='year',
            field=models.CharField(choices=[('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024'), ('2024-2025', '2024-2025')], default='none', max_length=20),
        ),
        migrations.AlterField(
            model_name='admissionstatistics',
            name='year',
            field=models.CharField(choices=[('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024'), ('2024-2025', '2024-2025')], default='none', max_length=20),
        ),
    ]
