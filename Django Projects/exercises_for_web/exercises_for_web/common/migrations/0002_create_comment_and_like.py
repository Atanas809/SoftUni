# Generated by Django 4.1.1 on 2022-10-17 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_create_photo'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.photo')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('publication_date_and_time', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='photos.photo')),
            ],
        ),
    ]
