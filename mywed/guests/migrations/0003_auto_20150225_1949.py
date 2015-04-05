# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0002_auto_20150225_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, verbose_name='Пользователь', related_name='guest_profile', blank=True),
        ),
    ]
