from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from mainapp import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('mainapp.urls')),
    path('', include('users.urls')),
    path('', include('comments.urls')),


    path('', views.home, name='home'),
    path('services/', views.service, name='service'),
    path('menu/', views.menu, name='menu'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('about/', views.about, name='about'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
