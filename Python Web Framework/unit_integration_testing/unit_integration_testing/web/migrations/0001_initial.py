# Generated by Django 4.1.3 on 2022-11-17 09:27

import django.core.validators
from django.db import migrations, models
import unit_integration_testing.web.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(150)])),
                ('egn', models.CharField(max_length=10, validators=[unit_integration_testing.web.models.egn_validator])),
            ],
        ),
    ]