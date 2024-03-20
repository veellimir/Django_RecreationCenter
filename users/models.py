from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Имя')
    username = models.CharField(max_length=100, blank=False, null=False, verbose_name='Логин')
    surname = models.CharField(max_length=50, blank=False, null=False, verbose_name='Фамилия')
    profile_image = models.ImageField(upload_to='profiles/',
                                      default='profiles/user.png', verbose_name='Изображения профиля')

    telegram = models.CharField(max_length=100, blank=True, null=True, verbose_name='telegram')
    vk = models.CharField(max_length=200, blank=True, null=True, verbose_name='vk')
    email = models.CharField(max_length=50, blank=False, null=False, verbose_name='email')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'пользователя'
        verbose_name_plural = 'Пользователи'
