from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=50, verbose_name='Названия')
    description = models.TextField(blank=False, null=False, verbose_name='Описания')
    feature_image = models.ImageField(upload_to='menu/%Y/%m/%d',
                                      default='default-services.jpg', verbose_name='Изображения')

    total = models.IntegerField(default=0, blank=True, null=True, verbose_name='')
    price = models.IntegerField(default=1000, blank=False, null=False, verbose_name='Цена за позицию')
    create = models.DateTimeField(auto_now_add=True, verbose_name='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'меню'


class Entertainment(models.Model):
    title = models.CharField(max_length=50, verbose_name='Названия')
    description = models.TextField(blank=False, null=False, verbose_name='Описания')
    feature_image = models.ImageField(upload_to='entertainment/%Y/%m/%d',
                                      default='default-services.jpg', verbose_name='Изображения')

    total = models.IntegerField(default=0, blank=True, null=True)
    price = models.IntegerField(default=10000, blank=False, null=False, verbose_name='Цена за позицию')
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'развлечение'
        verbose_name_plural = 'Развлечения'


class Services(models.Model):
    title = models.CharField(max_length=50, verbose_name='Названия')
    description = models.TextField(blank=False, null=False, verbose_name='Описания')
    feature_image = models.ImageField(upload_to='services/%Y/%m/%d',
                                      default='default-services.jpg', verbose_name='Изображения')

    tags = models.ManyToManyField('Tag', blank=True)
    total = models.IntegerField(default=0, blank=True, null=True)
    price = models.IntegerField(default=10000, blank=False, null=False, verbose_name='Цена за позицию/руб.')
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'дом'
        verbose_name_plural = 'Дома'


class Tag(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'Теги'


class InfoSlider(models.Model):
    description = models.TextField(max_length=100, blank=False, null=False, verbose_name='Описание слайда')
    image_slider = models.ImageField(upload_to='slider_images/%Y/%m/%d', blank=False,
                                     null=False, verbose_name='Изображения слайда')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'слайд'
        verbose_name_plural = 'Слайды'