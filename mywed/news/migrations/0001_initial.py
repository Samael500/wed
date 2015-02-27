# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Заголовок', max_length=200, blank=True, null=True)),
                ('text', models.TextField(max_length=1000, verbose_name='Содержание новости')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата публикации')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения')),
            ],
            options={
                'verbose_name_plural': 'Новости',
                'verbose_name': 'Новость',
            },
            bases=(models.Model,),
        ),
    ]
