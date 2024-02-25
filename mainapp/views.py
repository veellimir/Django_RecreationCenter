from django.shortcuts import render


from .models import Services, InfoSlider, Menu, Entertainment
from comments.models import Comments
from users.models import Profile
from .utils import search, dynamic_card, pagination


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
    custom_range, services = pagination(request, services, 3)

    context = {
        'services': services,
        'search_query': search_query,
        'custom_range': custom_range
    }
    return render(request, 'mainapp/services-page.html', context)


def menu(request):
    menu_card, search_query = search(request, 'menu')
    custom_range, menu_card = pagination(request, menu_card, 3)

    context = {
        'menu_card': menu_card,
        'search_query': search_query,
        'custom_range': custom_range
    }
    return render(request, 'mainapp/menu-pages.html', context)


def entertainment(request):
    entertainment_card, search_query = search(request, 'entertainment')
    custom_range, entertainment_card = pagination(request, entertainment_card, 3)

    context = {
        'entertainment_card': entertainment_card,
        'search_query': search_query,
        'custom_range': custom_range
    }
    return render(request, 'mainapp/entertainment-pages.html', context)


def cards_page(request, pk, card_type):
    card = dynamic_card(request, pk, card_type)
    return render(request, 'mainapp/cards.html', {'card': card})


def about(request):
    return render(request, 'mainapp/about.html')

