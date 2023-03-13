from __future__ import unicode_literals
from django.http import HttpResponseNotAllowed
from django.http import HttpResponse, JsonResponse
from django_daraja.mpesa.core import MpesaClient
from decouple import config
from django.shortcuts import render, redirect
from django_daraja.views import stk_push_callback_url
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from shoe.forms import ShoesForm
from shoe.models import Shoes




# Create your views here.
def new(request):
    if request.method == 'POST':
        form = ShoesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = ShoesForm()
    return render(request, 'index.html', {'form': form})

def show(request):
    shoes = Shoes.objects.all()
    return render(request, 'show.html', {'shoes': shoes})

def edit(request, id):
    shoes = Shoes.objects.get(id=id)
    return render(request, 'edit.html', {'shoes': shoes})

def update(request, id):
    shoes = Shoes.objects.get(id=id)
    form = ShoesForm(request.POST, instance=shoes)
    if form.is_valid():
        form.save()
        return redirect('/show')

    return redirect(request, 'edit.html', {'shoes': shoes})

def checkout(request, id):
    if request.method == 'POST':
        price = request.POST.get('shoe_price')
        phone_number = request.POST.get('phone_number')
        shoe_id = id  # set the shoe ID to the specified ID
        cl = MpesaClient()
        account_reference = 'Enterprise Shoes'
        transaction_desc = 'Paying for shoes'
        callback_url = request.build_absolute_uri(reverse('payment_callback'))  # use a dynamic callback URL
        try:
            response = cl.stk_push(phone_number, price, account_reference, shoe_id, transaction_desc, callback_url)
            return JsonResponse(response.response_description, safe=False)
        except:
            return JsonResponse({'message': 'An error occurred while processing your request. Please try again.'}, status=500)
    else:
        shoe = Shoes.objects.get(id=id)
        return render(request, 'checkout.html', {'shoe': shoe})



@csrf_exempt
def payment_callback(request):
    if request.method == 'POST':
        # extract the payment details from the request
        # verify the payment using the Safaricom API
        # update the payment status in your application
        return HttpResponse('Payment received.')
    else:
        return HttpResponseNotAllowed(['POST'])





def  stk_push_success(request):
    cl = MpesaClient()
    phone_number = config('LNM_PHONE_NUMBER')
    amount = 1
    account_reference = 'Enterprise Shoes'
    transaction_desc = 'Paying for shoes'
    callback_url = stk_push_callback_url
    r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return JsonResponse(r.response_description, safe=False)


def destroy(request, id):
    shoes = Shoes.objects.get(id=id)
    shoes.delete()
    return redirect('/show')

