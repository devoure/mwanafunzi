from django.db import models
from invoice.models import Invoice

# Create your models here.
class CardPayment(models.Model):
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE) 
    paid = models.BooleanField(default=False)
