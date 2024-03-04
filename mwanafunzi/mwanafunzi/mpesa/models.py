from django.db import models
from django.contrib.auth.models import User
from invoice.models import Invoice

# Create your models here.
class Payment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE)
