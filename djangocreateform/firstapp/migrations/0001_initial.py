# Generated by Django 2.2 on 2019-12-04 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=30)),
                ('esal', models.IntegerField()),
                ('eaddr', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
