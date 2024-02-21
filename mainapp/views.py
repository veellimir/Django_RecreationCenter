from django.shortcuts import render
from .models import Services, InfoSlider, Menu, Entertainment
from comments.models import Comments

from users.models import Profile
from .utils import search


def home(request):
    info_slider = InfoSlider.objects.all()

    services = Services.objects.all()
    menu_card = Menu.objects.all()
    entertainment_card = Entertainment.objects.all()

    comments = Comments.objects.all().order_by('-created')
    profiles = Profile.objects.values_list('profile_image', flat=True)

    context = {
        'services': services,
        'info_slider': info_slider,
        'menu_card': menu_card,
        'entertainment_card': entertainment_card,
        'comments': comments,
        'profiles': profiles
    }
    return render(request, 'mainapp/home.html', context)


def service(request):
    services, search_query = search(request, 'services')
    context = {
        'services': services,
        'search_query': search_query
    }
    return render(request, 'mainapp/services-page.html', context)


def menu(request):
    menu_card, search_query = search(request, 'menu')
    context = {
        'menu_card': menu_card,
        'search_query': search_query
    }
    return render(request, 'mainapp/menu-pages.html', context)


def entertainment(request):
    entertainment_card, search_query = search(request, 'entertainment')
    context = {
        'entertainment_card': entertainment_card,
        'search_query': search_query
    }
    return render(request, 'mainapp/entertainment-pages.html', context)


def cards_page(request, pk):
    services = Services.objects.get(id=pk)

    return render(request, 'mainapp/cards.html', {'services': services})


def about(request):
    return render(request, 'mainapp/about.html')

