from django.db import models


class StatusSupport(models.Model):
    status = models.CharField(max_length=50, verbose_name='Название статуса')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'Статус'


class Support(models.Model):
    sp_name = models.CharField(max_length=50, verbose_name='Имя')
    sp_phone = models.CharField(max_length=50, verbose_name='Номер телефона')
    sp_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    sp_status = models.ForeignKey(StatusSupport, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Статус')

    def __str__(self):
        return self.sp_name

    class Meta:
        verbose_name = 'поддержку'
        verbose_name_plural = 'Поддержка'


class CommentSupport(models.Model):
    comment_binding = models.ForeignKey(Support, on_delete=models.CASCADE, verbose_name='Обращение')
    comment_text = models.TextField(verbose_name='Комментарий')
    comment_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарий'
