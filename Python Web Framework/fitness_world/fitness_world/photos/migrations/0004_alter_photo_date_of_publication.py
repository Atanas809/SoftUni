# Generated by Django 4.1.3 on 2022-11-20 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_photo_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date_of_publication',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
