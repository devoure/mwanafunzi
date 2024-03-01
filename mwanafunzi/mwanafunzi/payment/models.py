from django.db import models
from django.contrib.auth.models import User

from django.core.validators import RegexValidator

# Create your models here.
class PaymentForm(models.Model):
  SPONSORSHIP_CHOICES = [
      ('SP', 'Self Sponsored'),
      ('GP', 'Government Sponsored')
  ]
  COURSE_CHOICES = [
      ('CT', 'Computer Technology'),
      ('CS', 'Computer Science')
  ]
  YEAR_CHOICES = [
      ('1', '1st Year'),
      ('2', '2nd Year'),
      ('3', '3rd Year'),
      ('4', '4th Year'),
      ('5', '5th Year'),
      ('6', '6th Year')
  ]
  SEMESTER_CHOICES = [
      ('1', '1st Semester'),
      ('2', '2nd Semester'),
      ('3', '3rd Semester'),
  ]

  sponsorship = models.CharField(max_length=20, choices=SPONSORSHIP_CHOICES)
  course = models.CharField(max_length=20, choices=COURSE_CHOICES)
  year = models.CharField(max_length=20, choices=YEAR_CHOICES)
  semester = models.CharField(max_length=20, choices=SEMESTER_CHOICES)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
  phone_number = models.CharField(validators=[phone_regex], max_length=20)
  full_name = models.CharField(max_length=50)
  student = models.ForeignKey(User, on_delete=models.CASCADE)
