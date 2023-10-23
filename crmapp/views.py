from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from .forms import OrderForm, CreateUserForm, CustomerForm
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only


# Handles user registration. It displays the registration form,
# processes form submission, creates a new user account,
# and redirects to the login page upon successful registration.


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'crmapp/register.html', context)


# Manages user login. It displays the login form, processes login
# requests, and redirects users to the home page after successful login.
# Displays an error message for incorrect credentials.


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'crmapp/login.html', context)


# Logs out the currently authenticated user and redirects to the login page.


def logoutUser(request):
    logout(request)
    return redirect('login')


# The dashboard view accessible to authenticated users with admin privileges.
# Retrieves and displays order and customer statistics.


@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
                'orders': orders,
                'customers': customers,
                'total_orders': total_orders,
                'delivered': delivered,
                'pending': pending
            }

    return render(request, 'crmapp/dashboard.html', context)


# The user-specific dashboard, accessible to customers.
# Displays order statistics for the logged-in customer.


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
                'orders': orders,
                'total_orders': total_orders,
                'delivered': delivered,
                'pending': pending
            }

    return render(request, 'crmapp/user.html', context)


# Allows customers to update their account settings.
# Displays a form to update customer details.


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'crmapp/account_settings.html', context)


# Displays a list of products. Accessible to users with admin privileges.


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()

    return render(request, 'crmapp/products.html', {'products': products})


# Shows details about a specific customer, including their orders.
# Provides filtering functionality for orders.


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
                'customer': customer,
                'orders': orders,
                'order_count': order_count,
                'myFilter': myFilter
            }

    return render(request, 'crmapp/customer.html', context)


# Allows admin users to create new orders for a specific customer.


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(
        Customer,
        Order,
        fields=('product', 'status'),
        extra=10
    )
    customer = Customer.objects.get(id=pk)
    print('Customer:', customer)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'form': formset}
    return render(request, 'crmapp/order_form.html', context)


# Allows admin users to update order details.


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    print('ORDER:', order)
    if request.method == 'POST':

        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    print('I got here')
    return render(request, 'crmapp/order_form.html', context)


# Allows admin users to delete an order, with a confirmation prompt.


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'crmapp/delete.html', context)
