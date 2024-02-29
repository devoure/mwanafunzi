from django.db import models
from django.contrib.auth.models import User

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
  first_name = models.CharField(max_length=50)
  second_name = models.CharField(max_length=50)
  student = models.ForeignKey(User, on_delete=models.CASCADE)
