from django.contrib import admin
from .models import PaymentForm

# Register your models here.
class PaymentFormAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'student', 'phone_number')

admin.site.register(PaymentForm, PaymentFormAdmin)
