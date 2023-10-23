from django.http import HttpResponse
from django.shortcuts import redirect


# This function is a decorator that checks if a user is not authenticated.
# If the user is authenticated, it redirects them to the home page; otherwise,
# it allows them to access the specified view.


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


# This function is a decorator that checks if the user belongs to one
# of the specified roles (groups).
# If the user's group is in the list of allowed roles, it allows access to the
# view; otherwise, it denies access and displays a message.


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator


# This function is a decorator that restricts access to a view based on the
# user's group.
# If the user's group is customer, it redirects them to the user-page.
# If the user's group is admin, it allows them to access the view.


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('user-page')

        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_function
