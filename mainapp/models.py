from django.db import models


class Services(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=False, null=False)
    feature_image = models.ImageField(upload_to='services/%Y/%m/%d', default='default-services.jpj')
    tags = models.ManyToManyField('Tag', blank=True)
    total = models.IntegerField(default=0, blank=True, null=True)
    price = models.IntegerField(default=10000, blank=False, null=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
