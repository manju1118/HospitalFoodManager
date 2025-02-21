# Generated by Django 5.1.4 on 2025-01-09 09:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('diseases', models.TextField()),
                ('allergies', models.TextField()),
                ('room_number', models.IntegerField()),
                ('bed_number', models.IntegerField()),
                ('floor_number', models.IntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('contact_info', models.CharField(max_length=15)),
                ('emergency_contact', models.CharField(max_length=15)),
                ('additional_info', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DietChart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('morning_meal', models.TextField()),
                ('evening_meal', models.TextField()),
                ('night_meal', models.TextField()),
                ('special_instructions', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
    ]
