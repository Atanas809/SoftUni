# Generated by Django 4.1.2 on 2022-10-04 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_employees_last_name_alter_employees_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
