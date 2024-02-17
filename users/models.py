from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=100, blank=False, null=False)
    surname = models.CharField(max_length=50, blank=False, null=False)
    profile_image = models.ImageField(upload_to='profiles/', default='profiles/user.png')

    telegram = models.CharField(max_length=100, blank=True, null=True)
    vk = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=50, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username



