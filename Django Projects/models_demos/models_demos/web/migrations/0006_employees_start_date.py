# Generated by Django 4.1.2 on 2022-10-04 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_employees_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
