from django.db.models import Q

from .models import Services, Menu, Entertainment


def search(request, model):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    if model == 'services':
        services = Services.objects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(price__icontains=search_query)
        )
        return services, search_query

    elif model == 'menu':
        menu_card = Menu.objects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(price__icontains=search_query)
        )
        return menu_card, search_query

    elif model == 'entertainment':
        entertainment = Entertainment.objects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(price__icontains=search_query)
        )
        return entertainment, search_query



