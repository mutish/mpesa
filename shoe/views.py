from django.shortcuts import render, redirect
from django_daraja.views import stk_push_callback_url

from shoe.forms import ShoesForm
from shoe.models import Shoes
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
from decouple import config
from django.http import HttpResponse, JsonResponse

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
    form = Shoes(request.POST, instance=shoes)
    if form.is_valid():
        form.save()
        return redirect('/show')

    return redirect(request, 'edit.html', {'shoes': shoes})

def index(request):
    shoes = Shoes.objects.get(id=id)
    form = Shoes(request.POST, instance=shoes)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return redirect(request, 'checkout.html', {'shoes': shoes})

def  stk_push_success(request):
    cl = MpesaClient()
    phone_number = config('LNM_PHONE_NUMBER')
    amount = 1
    account_reference = 'Enterprise Shoes'
    transaction_desc = 'Paying for shoes'
    callback_url = stk_push_callback_url
    r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return JsonResponse(r.response_description, safe=False)




# def index(request, id):
#     shoes = Shoes.objects.get(id=id)
#     form = Shoes(request.POST, instance=shoes)
#     if form.is_valid():
#         form.save()
#         return redirect('/show')
#     return redirect(request, 'checkout.html', {'shoes': shoes})
#
#     cl = MpesaClient()
#     phone_number = '0745353600'
#     amount = 1
#     account_reference = 'ENTERPRISES'
#     transaction_desc = 'paying shoes'
#     callback_url = 'https://api.darajambili.com/express-payment'
#     response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
#     return HttpResponse(response)


def destroy(request, id):
    shoes = Shoes.objects.get(id=id)
    shoes.delete()
    return redirect('/show')

