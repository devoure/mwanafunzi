from django.shortcuts import render

# Create your views here.
def print_invoice(request):
    return render(request, 'invoice.html', {})
