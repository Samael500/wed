# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0003_auto_20150225_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='user_key',
            field=models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z\\d]{8}$', message='Код доступа должен состоять из 8 символов (английские буквы или цифры).')], verbose_name='Код доступа'),
        ),
    ]
