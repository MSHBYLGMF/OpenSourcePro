# Generated by Django 3.2.12 on 2023-12-17 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Edu_pro', '0004_auto_20231217_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer_name', models.CharField(blank=True, max_length=30, null=True)),
                ('IP_address', models.CharField(blank=True, max_length=30, null=True)),
                ('MAC_address', models.CharField(blank=True, max_length=30, null=True)),
                ('os_model', models.CharField(blank=True, choices=[('window_8', 'window_8'), ('window_10', 'window_10'), ('ubuntu', 'ubuntu'), ('linux', 'linux'), ('window_7', 'window_7')], max_length=30, null=True)),
                ('users_name', models.CharField(blank=True, max_length=30, null=True)),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('purchase_date', models.DateField(blank=True, null=True, verbose_name='Purchase Date(mm/dd/2019)')),
                ('timestamp', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='computer',
            name='os_model',
            field=models.CharField(blank=True, choices=[('window_8', 'window_8'), ('window_10', 'window_10'), ('ubuntu', 'ubuntu'), ('linux', 'linux'), ('window_7', 'window_7')], max_length=30, null=True),
        ),
    ]
