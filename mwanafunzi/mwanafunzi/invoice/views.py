from django.shortcuts import render

# Create your views here.
def print_invoice(request, pay_slip):
    
    return render(request, 'invoice.html', {})
