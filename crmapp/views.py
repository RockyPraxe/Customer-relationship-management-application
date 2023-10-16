from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    context = {'orders': orders, 'customers': customers}

    return render(request, 'crmapp/dashboard.html', context)


def products(request):
    products = Product.objects.all()

    return render(request, 'crmapp/products.html', {'products': products})


def customer(request):
    return render(request, 'crmapp/customer.html')


def order(request):
    return render(request, 'crmapp/order.html')
