from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Order 
from .models import refId
from zeep import Client


MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
amount = 0 # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = ''  # Optional
CallbackURL = 'http://localhost:8000/verify/' # Important: need to edit for realy server.

@login_required(login_url = 'authenticate/login')
def send_request(request):
    for pic in request.user.queue:
        amount += pic.price
    email = request.user.email
    result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        # show the Error to the User and redirect them to the site
        return HttpResponse('Error code: ' + str(result.Status))
        
def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            orders = Order.objects.filter(user = request.user, ref_id = '')
            for order in orders:
                order.change_ref_id(result.RefID)
            # # here we should redirect the user to the view that handels download link 
            # # and also we have to pass orders as context to the view
            # now that verification is Done we have to send the Download link to
            # the costumer and redirect him back to the site
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            orders = Order.objects.filter(user = request.user, ref_id = '')
            for order in orders:
                order.change_ref_id(result.RefID)
            # now that verification is Done we have to send the Download link to
            # the costumer and redirect him back to the site
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            # when we get to here means that verification went wrong and we have
            # to show the result.status to the costumer to inform him that what
            # went wrong in the procces
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        # when we get to here means that verification went wrong or user canceled
        # the procces
        return HttpResponse('Transaction failed or canceled by user')
