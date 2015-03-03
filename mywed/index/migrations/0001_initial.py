# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('kind', models.CharField(verbose_name='Тип страницы', choices=[('index', 'Главная страница'), ('contacts', 'Контакты')], unique=True, max_length=10)),
                ('title', models.CharField(verbose_name='Заголовок', max_length=200)),
                ('content', models.TextField(verbose_name='Содержание страницы')),
                ('created_at', models.DateTimeField(verbose_name='Время создания', auto_now_add=True)),
                ('modified_at', models.DateTimeField(verbose_name='Время последнего изменения', auto_now=True)),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
            bases=(models.Model,),
        ),
    ]
