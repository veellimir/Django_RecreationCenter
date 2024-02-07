from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from mainapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('logout_user/', views.logout_user, name='logout_user'),

    path('', include('mainapp.urls')),


    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('services/', views.service, name='service'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
