# Generated by Django 3.2.12 on 2023-12-21 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Edu_pro', '0007_auto_20231219_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='os_model',
            field=models.CharField(blank=True, choices=[('linux', 'linux'), ('window_8', 'window_8'), ('window_10', 'window_10'), ('window_7', 'window_7'), ('ubuntu', 'ubuntu')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='computerhistory',
            name='os_model',
            field=models.CharField(blank=True, choices=[('linux', 'linux'), ('window_8', 'window_8'), ('window_10', 'window_10'), ('window_7', 'window_7'), ('ubuntu', 'ubuntu')], max_length=30, null=True),
        ),
    ]
