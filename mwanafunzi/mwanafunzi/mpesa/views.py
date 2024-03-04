from django.shortcuts import render
import requests
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import hashlib
import hmac
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import authenticate
from invoice.models import Invoice
from .models import Payment

# Create your views here.
def initiate(request):
    access_token = authenticate()
    if access_token != None:
        invoice_id = request.session.get('invoice')['id']
        invoice = Invoice.objects.get(id=invoice_id)

        payload = {
          "BusinessShortCode": invoice.more,    
          "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTYwMjE2MTY1NjI3",    
          "Timestamp":"20160216165627",    
          "TransactionType": "CustomerPayBillOnline",    
          "Amount": str(invoice.fee_structure.fee).split(".")[0], 
          "PartyA": invoice.payment_slip.phone_number[1:],    
          "PartyB": invoice.more,    
          "PhoneNumber":invoice.payment_slip.phone_number[1:],    
          "CallBackURL": "https://d3d7-102-164-60-30.ngrok-free.app/mpesa/complete",    
          "AccountReference":"Dev University",    
          "TransactionDesc":"Test"
        }
        daraja_api_endpoint = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }
        try:
            response = requests.post(daraja_api_endpoint, json=payload, headers=headers)
            if response.status_code == 200:
                context = { 'invoice':invoice } 
                return render(request, 'mpesa_processing.html', context)
            else:
                return HttpResponse("ERROR sending POST: + {}".format(response.status_code) )
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return HttpResponse('Wrong Token')


@csrf_exempt
def complete(request):
    invoice = Invoice.objects.get(id = request.session.get('invoice')['id'])
    print("RUNNNED")
    if request.method == 'POST':
        consumer_secret = '0mUBFEcQsck6TRdvHVnS4NAJC14mxF91DSYctGVOR2m1Azv18qmKI9ZuTdgTJ08Q'
        # Extract the raw body of the request
        raw_data = request.body.decode('utf-8')

        # Extract the signature from the request headers
        signature = request.headers.get('X-Safaricom-Signature')

        # Calculate the expected signature using your API consumer secret
        expected_signature = hmac.new(
            consumer_secret.encode('utf-8'),
            raw_data.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

        # Compare the expected signature with the received signature
        if signature != expected_signature:
            return JsonResponse({'error': 'Invalid signature'}, status=400)

        # Parse the callback data as JSON
        data = json.loads(raw_data)

        # Process the callback data
        payment = Payment.objects.create(student=request.user, invoice=invoice)
        return render(request, 'mpesa_complete.html', {} )
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)   
