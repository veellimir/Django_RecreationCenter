from django.db import models

from users.models import Profile


class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='messages')
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=True, blank=True)
    telegram = models.TextField(max_length=50, null=False, blank=False)

    subject_msg = models.CharField(max_length=100, null=False, blank=False)
    body_msg = models.TextField()

    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject_msg

    class Meta:
        ordering = ['is_read', '-created']