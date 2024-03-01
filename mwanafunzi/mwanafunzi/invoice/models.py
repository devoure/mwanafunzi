from django.db import models
from django.contrib.auth.models import User
from payment.models import PaymentForm

# Create your models here.
class FeeStructure(models.Model):
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

    fee = models.DecimalField(max_digits=10, decimal_places=2) 
    sponsorship = models.CharField(max_length=20, choices=SPONSORSHIP_CHOICES)
    course = models.CharField(max_length=20, choices=COURSE_CHOICES)
    year = models.CharField(max_length=20, choices=YEAR_CHOICES)
    semester = models.CharField(max_length=20, choices=SEMESTER_CHOICES)

    def __str__(self):
        return "{}, {}, {}, {}".format(self.course, self.sponsorship, self.year, self.semester)


class Invoice(models.Model):
    PAY_CHOICES = [
        ('SF', 'Safaricom'),
        ('BK', 'Bank')
    ]

    SAF_SERVICES = [
        ('PC', 'Pochi La Biashara'),
        ('BG', 'Buy Goods'),
        ('PB', 'Pay Bill')
    ]
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    fee_structure = models.OneToOneField(FeeStructure, on_delete=models.CASCADE)
    payment_slip = models.OneToOneField(PaymentForm, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=20, choices=PAY_CHOICES)
    safaricom_service = models.CharField(max_length=20, choices=SAF_SERVICES)
    more = models.CharField(max_length=50)
