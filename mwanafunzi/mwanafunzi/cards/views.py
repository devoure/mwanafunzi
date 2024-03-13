from django.shortcuts import render, redirect
import braintree
from django.conf import settings
from invoice.models import Invoice
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


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

def send_email(request):
    invoice_id = request.session.get('invoice')['id']
    invoice = Invoice.objects.get(id=invoice_id)

    tempate = render_to_string('cards/email.html', { 'name' : request.user.last_name,
                                                    'invoice_number' : invoice.id,
                                                    'course': invoice.fee_structure.course.
                                                    'year': invoice.fee_structure.year,
                                                    'semester': invoice.fee_structure.semester,
                                                    'amount': invoice.fee_structure.fee})


    email = EmailMessage(
            'Dev University Fee Statement',
            template,
            settings.EMAIL_HOST_USER,
            ['mshewaathumanibakari@gmail.com']
            )
    email_fail_silently = False
    email.send()
