from django.contrib import admin
from .models import FeeStructure, Invoice

# Register your models here.
class FeeStructureAdmin(admin.ModelAdmin):
    list_display = ('course', 'semester', 'year', 'fee', 'sponsorship')


admin.site.register(FeeStructure, FeeStructureAdmin)

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('student', )


admin.site.register(Invoice, InvoiceAdmin)
