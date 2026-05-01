from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .form import UserForm


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):   # 👈 name change
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')


def logout_view(request):
    messages.success(request, 'You are now logged out')
    return redirect('login')