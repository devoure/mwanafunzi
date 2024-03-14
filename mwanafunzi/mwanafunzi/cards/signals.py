from django.db.models.signals import post_save
from .models import CardPayment
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

def send_email(sender, instance, **kwargs):
    print("Function called")
    template = render_to_string('email.html', { 'name' : instance.invoice.student.last_name,
                                                    'invoice_number' : instance.invoice.id,
                                                    'course': instance.invoice.fee_structure.course,
                                                    'year': instance.invoice.fee_structure.year,
                                                    'semester': instance.invoice.fee_structure.semester,
                                                    'amount': instance.invoice.fee_structure.fee})


    email = EmailMessage(
            'Dev University Fee Statement',
            template,
            settings.EMAIL_HOST_USER,
            ['mshewaathumanibakari@gmail.com']
            )
    email.fail_silently = False
    email.send()
    print("mail sent")

post_save.connect(send_email, sender=CardPayment)
