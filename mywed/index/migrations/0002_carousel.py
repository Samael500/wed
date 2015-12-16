# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100, blank=True, null=True, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=500, blank=True, null=True, verbose_name='Описание')),
                ('photo', models.ImageField(verbose_name='Фотография', upload_to='')),
            ],
            options={
                'verbose_name': 'Изображение в каруселе',
                'verbose_name_plural': 'Изображения в каруселе',
            },
            bases=(models.Model,),
        ),
    ]
