from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'crmapp/dashboard.html')


def products(request):
    return render(request, 'crmapp/products.html')


def customer(request):
    return render(request, 'crmapp/customer.html')


def order(request):
    return render(request, 'crmapp/order.html')
