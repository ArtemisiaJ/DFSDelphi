# Generated by Django 5.0.2 on 2024-02-29 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DigitalForensicHub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Practitioner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(default='PSE', max_length=10)),
                ('force_number', models.CharField(max_length=10, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offence', models.CharField(max_length=50)),
                ('status', models.CharField(default='', max_length=50)),
                ('hub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.digitalforensichub')),
                ('practitioner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.practitioner')),
            ],
        ),
    ]
