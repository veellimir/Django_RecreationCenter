from django.forms import ModelForm

from .models import Comments


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['user_comments']