# Generated by Django 3.2.12 on 2023-12-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Edu_pro', '0003_auto_20231217_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='purchase_date',
            field=models.DateField(blank=True, null=True, verbose_name='Purchase Date(mm/dd/2019)'),
        ),
        migrations.AddField(
            model_name='computer',
            name='timestamp',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='os_model',
            field=models.CharField(blank=True, choices=[('window_7', 'window_7'), ('window_10', 'window_10'), ('window_8', 'window_8'), ('linux', 'linux'), ('ubuntu', 'ubuntu')], max_length=30, null=True),
        ),
    ]