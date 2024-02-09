from django.shortcuts import render

from .models import Services, Tag


def home(request):
    services = Services.objects.all()
    context = {'services': services}
    return render(request, 'mainapp/home.html', context)


def service(request):
    services = Services.objects.all()
    context = {'services': services}
    return render(request, 'mainapp/services-page.html', context)
