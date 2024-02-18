from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Comments


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['user_comments']