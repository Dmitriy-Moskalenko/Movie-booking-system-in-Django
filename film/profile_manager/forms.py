from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from profile_manager.models import Ticket


class RegistrationForm(UserCreationForm):
    """Форма регистрации"""
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    """Форма авторизации"""
    username = forms.CharField()
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'password']


class TicketForm(forms.ModelForm):
    """Форма бронирования билетов"""
    row = forms.IntegerField(required=False, label='',
                             widget=forms.NumberInput(attrs={'id': 'row_id', 'readonly': 'True'}))
    seat = forms.IntegerField(required=False, label='',
                              widget=forms.NumberInput(attrs={'id': 'seat_id', 'readonly': 'True'}))

    class Meta:
        model = Ticket
        fields = ['row', 'seat']



