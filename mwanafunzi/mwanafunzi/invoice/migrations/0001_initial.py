# Generated by Django 5.0.2 on 2024-03-01 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeeStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sponsorship', models.CharField(choices=[('SP', 'Self Sponsored'), ('GP', 'Government Sponsored')], max_length=20)),
                ('course', models.CharField(choices=[('CT', 'Computer Technology'), ('CS', 'Computer Science')], max_length=20)),
                ('year', models.CharField(choices=[('1', '1st Year'), ('2', '2nd Year'), ('3', '3rd Year'), ('4', '4th Year'), ('5', '5th Year'), ('6', '6th Year')], max_length=20)),
                ('semester', models.CharField(choices=[('1', '1st Semester'), ('2', '2nd Semester'), ('3', '3rd Semester')], max_length=20)),
            ],
        ),
    ]
