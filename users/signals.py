from django.db.models.signals import post_save
from django.contrib.auth.models import User

from .models import Profile


def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            name=user.username,
            surname=user.last_name,
            email=user.email
        )
    return False


post_save.connect(create_profile, sender=User)
