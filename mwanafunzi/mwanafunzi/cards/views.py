from django.shortcuts import render
import braintree
from django.conf import settings

# Create your views here.
gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

def process(request):
    if request.method == 'POST':
        nonce = request.POST.get('payment_method_nonce', None)
        res = gateway.transaction.sale({
            'amount': 200,
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement':True
                }
            })


def failed(request):
    pass

def done(request):
    pass

