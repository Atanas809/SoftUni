# Generated by Django 4.1.2 on 2022-10-05 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_employees_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='level',
            field=models.CharField(max_length=15),
        ),
    ]