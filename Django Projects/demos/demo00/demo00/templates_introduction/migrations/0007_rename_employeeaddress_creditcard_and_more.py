# Generated by Django 4.1.1 on 2022-10-05 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templates_introduction', '0006_employeeaddress'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmployeeAddress',
            new_name='CreditCard',
        ),
        migrations.RenameField(
            model_name='creditcard',
            old_name='address',
            new_name='owner',
        ),
    ]