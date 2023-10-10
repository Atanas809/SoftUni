# Generated by Django 4.1.2 on 2022-10-10 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Address'},
        ),
        migrations.AddField(
            model_name='student',
            name='level',
            field=models.CharField(choices=[('Junior', 'Junior'), ('Mid', 'Mid'), ('Regular', 'Regular'), ('Senior', 'Senior')], default='Junior', max_length=30),
            preserve_default=False,
        ),
    ]
