# Generated by Django 5.0.2 on 2024-03-01 06:04

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsorship', models.CharField(choices=[('SP', 'Self Sponsored'), ('GP', 'Government Sponsored')], max_length=20)),
                ('course', models.CharField(choices=[('CT', 'Computer Technology'), ('CS', 'Computer Science')], max_length=20)),
                ('year', models.CharField(choices=[('1', '1st Year'), ('2', '2nd Year'), ('3', '3rd Year'), ('4', '4th Year'), ('5', '5th Year'), ('6', '6th Year')], max_length=20)),
                ('semester', models.CharField(choices=[('1', '1st Semester'), ('2', '2nd Semester'), ('3', '3rd Semester')], max_length=20)),
                ('phone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('full_name', models.CharField(max_length=50)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
