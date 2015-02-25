from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Guest(models.Model):

    """ My wedding guest's """

    user = models.ForeignKey(User, verbose_name='Пользователь', blank=True, null=True)
    user_key = models.CharField(verbose_name='Код доступа', max_length=8, unique=True, validators=[RegexValidator(
        '^[\w\d]{8}$', message='Код доступа должен состоять из 8 символов (английские буквы или цифры).')])

    def save(self, *args, **kwargs):
        """ create user on save """
        if not self.pk and self.user is None:
            self.user = User.objects.create_user(username=self.user_key, password=self.user_key)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name='Гость'
        verbose_name_plural='Гости'
