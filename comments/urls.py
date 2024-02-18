from django.urls import path
from comments import views

urlpatterns = [
    path('comments/', views.comment_user, name='comments')
]