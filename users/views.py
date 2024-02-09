from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from .models import Profile


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        username = request.POST['username']
        # username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            print('Имя пользователя не существует')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        print('Неверный логин или пароль')
    return render(request, 'users/register_login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required()
def profile(request):
    return render(request, 'users/profile.html')