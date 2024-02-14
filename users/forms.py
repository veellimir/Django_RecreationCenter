from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'email',
            'username',
            'password1',
            'password2'
        ]

        labels = {
            'first_name': 'Имя',
            'email': 'Email',
            'username': 'Логин',
            'password1': 'Пароль',
            'password2': 'Повторить пароль'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input_auth'})