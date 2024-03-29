# Generated by Django 4.1.1 on 2022-10-17 09:34

import django.core.validators
from django.db import migrations, models
import exercises_for_web.photos.validations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_create_pet'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', validators=[exercises_for_web.photos.validations.validate_image_size])),
                ('description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('publication_date', models.DateField(auto_now=True)),
                ('tagged_pets', models.ManyToManyField(blank=True, null=True, to='pets.pet')),
            ],
        ),
    ]
