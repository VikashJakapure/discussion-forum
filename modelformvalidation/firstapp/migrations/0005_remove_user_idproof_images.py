# Generated by Django 2.2.7 on 2020-01-10 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20200110_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='idproof_images',
        ),
    ]
