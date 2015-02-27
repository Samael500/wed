# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150227_2231'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-pub_date', '-created_at'), 'verbose_name_plural': 'Новости', 'verbose_name': 'Новость'},
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата публикации'),
        ),
    ]
