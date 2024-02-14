from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile
from .forms import CustomUserRegisterForm


def register_user(request):
    """the function references the same page register_login.html"""
    page = 'register'
    form = CustomUserRegisterForm(request.POST)
    show_footer = False

    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            # user.username = user.username.lower()
            user.username = user.username
            user.save()

            messages.success(request, f'Добро пожаловать {user}')
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'При регистрации произошла ошибка')

    context = {'page': page, 'form': form, 'show_footer': show_footer}
    return render(request, 'users/register_login.html', context)


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
            messages.error(request, 'Имя пользователя не существует')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        print('Неверный логин или пароль')
        messages.error(request, 'Неверный пароль')
    return render(request, 'users/register_login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def profile(request):
    prof = request.user.profile
    context = {'profile': prof}

    return render(request, 'users/profile.html', context)

