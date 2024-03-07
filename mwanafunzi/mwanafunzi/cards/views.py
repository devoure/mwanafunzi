from django.shortcuts import render, redirect
import braintree
from django.conf import settings
from invoice.models import Invoice

# Create your views here.
gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

def process(request):
    invoice_id = request.session.get('invoice')['id']
    invoice = Invoice.objects.get(id=invoice_id)

    if request.method == 'POST':
        nonce = request.POST.get('payment_method_nonce', None)
        res = gateway.transaction.sale({
            'amount': str(invoice.fee_structure.fee),
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement':True
                }
            })
        if res.is_success:
            return redirect('braintree-done')
        else:
            errors_mes = ""
            for error in res.errors.deep_errors:
                print(errors_mes + error.code + error.message)
            return redirect('braintree-failed')
    else:
        token = gateway.client_token.generate()
        context = {'token':token}
        return render(request, 'process.html', context)


def failed(request):
    return render(request, 'failed.html')

def done(request):
    return render(request, 'done.html')
