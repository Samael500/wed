# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('user_key', models.CharField(max_length=8, unique=True, verbose_name='Код доступа', validators=[django.core.validators.RegexValidator('^[\\w\\d]{8}$', message='Код доступа должен состоять из 8 символов (английские буквы или цифры).')])),
                ('user', models.ForeignKey(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Гость',
                'verbose_name_plural': 'Гости',
            },
            bases=(models.Model,),
        ),
    ]
