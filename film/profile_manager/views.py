from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from profile_manager.forms import RegistrationForm, LoginForm
from profile_manager.models import Ticket


def registration(request):
    """Регистрация пользователей"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegistrationForm(request.POST)
    return render(request, 'registration.html', {'form': form})


def login_(request):
    """Авторизация пользователей"""
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = LoginForm(data=request.POST)
    return render(request, 'login.html', {'form': form})


def logout_(request):
    """Выход из аккаунта"""
    logout(request)
    return redirect('/')


def my_tickets(request):
    """Странца с моими билетами"""
    my_tickets_ = Ticket.objects.filter(user=request.user)
    return render(request, 'my_tickets.html', {'my_tickets': my_tickets_})

