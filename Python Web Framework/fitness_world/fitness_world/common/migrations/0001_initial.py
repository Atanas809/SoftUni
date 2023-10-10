# Generated by Django 4.1.3 on 2022-11-20 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0003_alter_photo_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='photos.photo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]