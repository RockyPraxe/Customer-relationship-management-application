from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def home(request):
    return render(request, 'crmapp/dashboard.html')


def products(request):
    products = Product.objects.all()
    return render(request, 'crmapp/products.html', {'products': products})


def customer(request):
    return render(request, 'crmapp/customer.html')


def order(request):
    return render(request, 'crmapp/order.html')
