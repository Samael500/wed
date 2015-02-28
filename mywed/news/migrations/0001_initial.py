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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(verbose_name='Заголовок', max_length=200)),
                ('text', models.TextField(verbose_name='Содержание новости', max_length=1000)),
                ('pub_date', models.DateField(verbose_name='Дата публикации', default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(verbose_name='Время создания', auto_now_add=True)),
                ('modified_at', models.DateTimeField(verbose_name='Время последнего изменения', auto_now=True)),
            ],
            options={
                'verbose_name': 'Новость',
                'ordering': ('-pub_date', '-created_at'),
                'verbose_name_plural': 'Новости',
            },
            bases=(models.Model,),
        ),
    ]
