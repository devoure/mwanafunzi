from django.shortcuts import render
from .models import FeeStructure, Invoice
from payment.models import PaymentForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize


# Create your views here.
@login_required(login_url='login')
def print_invoice(request):
    pay_slip = request.session.get('pay_slip')
    slip_instance = PaymentForm.objects.get(id=pay_slip['id'])
    till = '174379'
    try:
        fee_structure = FeeStructure.objects.get(sponsorship=pay_slip['sponsorship'],
                                                 course=pay_slip['course'],
                                                 year=pay_slip['year'],
                                                 semester=pay_slip['semester'])


    except FeeStructure.DoesNotExist:
        fee_structure = None
        slip_instance.delete()
        return render(request, 'badinvoice.html')
        

    

    try:
        invoice = Invoice.objects.create(student=request.user,
                                         fee_structure=fee_structure,
                                         payment_slip=slip_instance,
                                         payment_type=Invoice.PAY_CHOICES[0][0],
                                         safaricom_service=Invoice.SAF_SERVICES[1][0],
                                         more=till)

        request.session['invoice'] = {'id':invoice.pk}
    except IntegrityError:
        invoice = Invoice.objects.get(payment_slip=slip_instance)

    context = {'invoice':invoice}



    
    return render(request, 'invoice.html', context)
