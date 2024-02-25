from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Profile


class CustomUserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            # 'first_name',
            # 'email',
            'username',
            'password1',
            'password2'
        ]

        labels = {
            # 'first_name': 'Имя',
            # 'email': 'Email',
            'username': 'Логин',
            'password1': 'Пароль',
            'password2': 'Повторить пароль'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input_auth'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'username',
            'name',
            'surname',
            'email',
            'profile_image',
            'telegram',
            'vk'
        ]

        labels = {
            'username': 'Логин',
            'name': 'Имя',
            'surname': 'Фамилия',
            'email': 'Email',
            'profile_image': 'Изображение профиля',
            'telegram': 'Телеграм',
            'vk': 'ВКонтакте',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input_auth'})