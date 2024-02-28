from django.shortcuts import render, redirect

from .forms import CreateUserForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user

# Create your views here.


@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            new_user = form.cleaned_data.get('last_name')
            messages.success(request, 'Welcome ' + new_user + ' , You can Login')
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Something went wrong, try again')
    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect('login')
