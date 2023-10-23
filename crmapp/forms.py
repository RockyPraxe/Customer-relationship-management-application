from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


# CustomerForm class is a ModelForm used to create and update customer records.


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


# OrderForm class is a ModelForm designed for managing orders, it is linked to
# the Order.


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


# CreateUserForm class extends Django's UserCreationForm
# It's used for user registration


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
