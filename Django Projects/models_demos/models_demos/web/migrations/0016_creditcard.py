# Generated by Django 4.1.2 on 2022-10-05 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_projects_alter_employees_department_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
