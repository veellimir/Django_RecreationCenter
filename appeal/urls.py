from django.urls import path
from appeal import views

urlpatterns = [
    path('appeal/', views.appeal_page, name='appeal'),

    path('chat_message/<str:pk>/', views.appeal_views, name='chat_message')
]