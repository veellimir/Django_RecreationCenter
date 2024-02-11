from django.shortcuts import render

from .models import Services, InfoSlider, Menu, Entertainment


def home(request):
    info_slider = InfoSlider.objects.all()
    services = Services.objects.all()
    menu_card = Menu.objects.all()
    entertainment_card = Entertainment.objects.all()
    context = {
        'services': services,
        'info_slider': info_slider,
        'menu_card': menu_card,
        'entertainment_card': entertainment_card
    }
    return render(request, 'mainapp/home.html', context)


def service(request):
    services = Services.objects.all()
    context = {'services': services}
    return render(request, 'mainapp/services-page.html', context)


def menu(request):
    menu_card = Menu.objects.all()
    context = {'menu_card': menu_card}
    return render(request, 'mainapp/menu-pages.html', context)


def entertainment(request):
    entertainment_card = Entertainment.objects.all()
    context = {'entertainment_card': entertainment_card}
    return render(request, 'mainapp/entertainment-pages.html', context)


def about(request):
    return render(request, 'mainapp/about.html')