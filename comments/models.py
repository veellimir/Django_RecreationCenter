from django.db import models

from users.models import Profile


class Comments(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    user_comments = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_comments

    class Meta:
        unique_together = ['owner']