from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(app_view):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return app_view(request, *args, **kwargs)
    return wrapper_func
