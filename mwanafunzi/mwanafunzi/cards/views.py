from django.shortcuts import render, redirect
import braintree
from django.conf import settings
from invoice.models import Invoice
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from cards.models import CardPayment
from cards.signals import send_email

# Create your views here.
gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

def process(request):
    invoice_id = request.session.get('invoice')['id']
    invoice = Invoice.objects.get(id=invoice_id)
    new_card_payment = CardPayment(invoice=invoice, paid=True)
    new_card_payment.save()



#    if request.method == 'POST':
#        nonce = request.POST.get('payment_method_nonce', None)
#        res = gateway.transaction.sale({
#            'amount': str(invoice.fee_structure.fee),
#            'payment_method_nonce': nonce,
#            'options': {
#                'submit_for_settlement':True
#                }
#            })
#        if res.is_success:
#            new_card_payment = CardPayment(invoice=invoice, paid=True)
#            new_card_payment.save()
#            return redirect('braintree-done')
#        else:
#            errors_mes = ""
#            for error in res.errors.deep_errors:
#                print(errors_mes + error.code + error.message)
#            return redirect('braintree-failed')
#    else:
#        token = gateway.client_token.generate()
#        context = {'token':token}
#        return render(request, 'process.html', context)


def failed(request):
    return render(request, 'failed.html')

def done(request):
    return render(request, 'done.html')
