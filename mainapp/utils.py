from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Services, Menu, Entertainment


def search(request, model):
    """
    function for dynamic search

    params:
    request: Объект запроса
    model: Параметр выбранной страницы (например, 'services', 'menu', 'entertainment')
    """

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


def dynamic_card(request, pk, card_type):
    """
    function for dynamic service pages.

    params:
    request: Объект запроса
    pk (str): id объекта
    card_type (str): Тип объекта (например, 'services', 'menu', 'entertainment')
    """

    if card_type == 'services':
        card = Services.objects.get(id=pk)
        return card
    elif card_type == 'menu':
        card = Menu.objects.get(id=pk)
        return card
    elif card_type == 'entertainment':
        card = Entertainment.objects.get(id=pk)
        return card
    else:
        card = None
    return card


def pagination(request, items, result):
    """
    function for dynamic pagination

    params:
    request: Объект запроса
    items: Параметр объекта/страницы
    result: Кол-во карточек на странице
    """

    page = request.GET.get('page')
    paginator = Paginator(items, result)

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        items = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        items = paginator.page(page)

    left_index = int(page) - 3
    right_index = int(page) + 4

    if left_index < 1:
        left_index = 1

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)
    return custom_range, items
