from django.contrib import admin
from .models import PaymentForm

# Register your models here.
class PaymentFormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'student')

admin.site.register(PaymentForm, PaymentFormAdmin)
