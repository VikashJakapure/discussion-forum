# Generated by Django 2.2.7 on 2020-01-23 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.AutoField(primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=36)),
            ],
        ),
        migrations.CreateModel(
            name='IdProof',
            fields=[
                ('idproof_id', models.AutoField(primary_key=True, serialize=False)),
                ('idproof_type', models.CharField(max_length=36)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.AutoField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=36)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.Country')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=36)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.State')),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('area_id', models.AutoField(primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=36)),
                ('area_pincode', models.IntegerField(unique=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.City')),
            ],
        ),
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=36)),
                ('admin_username', models.CharField(max_length=36, unique=True)),
                ('admin_password', models.CharField(max_length=36)),
                ('admin_confirm_password', models.CharField(max_length=36)),
                ('admin_email', models.EmailField(max_length=254)),
                ('admin_contact', models.IntegerField(unique=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.Area')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.Country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.State')),
            ],
        ),
    ]
