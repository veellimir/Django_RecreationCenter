# Generated by Django 5.0.3 on 2024-03-20 17:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('username', models.CharField(max_length=100, verbose_name='Логин')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('profile_image', models.ImageField(default='profiles/user.png', upload_to='profiles/', verbose_name='Изображения профиля')),
                ('telegram', models.CharField(blank=True, max_length=100, null=True, verbose_name='telegram')),
                ('vk', models.CharField(blank=True, max_length=200, null=True, verbose_name='vk')),
                ('email', models.CharField(max_length=50, verbose_name='email')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'пользователя',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
