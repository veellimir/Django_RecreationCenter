from sqlite3 import InternalError

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def sign_up(request):
    if request.method == 'GET':
        return render(request,
                      'mainapp/sign_up.html',
                      {'form_auth': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password1']:
            try:
                user = User.objects.create_user(
                                                request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except InternalError:
                return render(request,
                              'mainapp/sign_up.html',
                              {'form_auth': UserCreationForm(),
                               'error_auth': 'Имя пользователя уже существует'})
        else:
            return render(request,
                          'mainapp/sign_up.html',
                          {'form_auth': UserCreationForm(),
                           'error_auth': 'Пароли не совпадают'})


def sign_in(request):
    if request.method == 'GET':
        return render(request, 'mainapp/sign_in.html', {'form_auth': AuthenticationForm()})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request,
                          'mainapp/sign_in.html',
                          {'form_auth': AuthenticationForm(),
                           'error_auth': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('home')


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('sign_in')


def home(request):
    return render(request, 'mainapp/home.html')


@login_required()
def profile(request):
    return render(request, 'mainapp/profile.html')
