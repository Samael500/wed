from django.db import models
from datetime import datetime


class News(models.Model):

    """ News model """

    title = models.CharField(verbose_name='Заголовок', max_length=200)
    text = models.TextField(verbose_name='Содержание новости', max_length=1000)
    pub_date = models.DateField(verbose_name='Дата публикации', default=datetime.now)
    photo = models.ImageField(verbose_name='Фотография', blank=True, null=True)

    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name='Время последнего изменения', auto_now=True)

    def __str__(self):
        return '{date}: {title}'.format(date=self.pub_date, title=self.title)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('-pub_date', '-created_at')
