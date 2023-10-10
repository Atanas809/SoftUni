# Generated by Django 4.1.2 on 2022-10-30 07:46

import django.core.validators
from django.db import migrations, models
import web_final_exam_2022.cars.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(choices=[('Sports Car', 'Sports Car'), ('Pickup', 'Pickup'), ('Crossover', 'Crossover'), ('Minibus', 'Minibus'), ('Other', 'Other')], max_length=10)),
                ('model', models.CharField(max_length=20, validators=[web_final_exam_2022.cars.validators.validate_model])),
                ('year', models.IntegerField(validators=[web_final_exam_2022.cars.validators.validate_year_in_range])),
                ('image_url', models.URLField()),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]