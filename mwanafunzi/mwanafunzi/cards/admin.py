from django.contrib import admin
from .models import CardPayment

# Register your models here.
class CardPaymentAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'paid')


admin.site.register(CardPayment, CardPaymentAdmin)
