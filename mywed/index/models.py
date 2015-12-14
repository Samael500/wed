from django.db import models


class WebPage(models.Model):

    """ WebPage model """

    INDEX = 'index'
    CONTACTS = 'contacts'

    KIND_CHOICES = (
        (INDEX, 'Главная страница'),
        (CONTACTS, 'Контакты'), )

    kind = models.CharField(verbose_name='Тип страницы', choices=KIND_CHOICES, max_length=10, unique=True)
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    content = models.TextField(verbose_name='Содержание страницы')

    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name='Время последнего изменения', auto_now=True)

    def __str__(self):
        return '{kind}: {title}'.format(kind=self.get_kind_display(), title=self.title)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class Carousel(models.Model):

    """ Carousel photos model """

    title = models.CharField(verbose_name='Заголовок', max_length=100, blank=True, null=True)
    description = models.CharField(verbose_name='Описание', max_length=500, blank=True, null=True)
    photo = models.ImageField(verbose_name='Фотография')

    def __str__(self):
        return self.title or 'no name'

    class Meta:
        verbose_name = 'Изображение в каруселе'
        verbose_name_plural = 'Изображения в каруселе'
