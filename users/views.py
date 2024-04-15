from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from users.forms import LoginUsersForm


class LoginUser(LoginView):
    form_class = LoginUsersForm
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Авторизация'
    }

def logout_view(request):
    return HttpResponse("logout")