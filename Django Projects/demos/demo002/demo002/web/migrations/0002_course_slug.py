# Generated by Django 4.1.2 on 2022-10-10 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
