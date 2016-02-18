from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from guests.models import Guest


class LoginForm(forms.Form):

    """ Form for login guests """

    user_key = forms.CharField(
        required=True, max_length=8, label=Guest._meta.get_field_by_name('user_key')[0].verbose_name)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_errors_css()
        self.fields['user_key'].widget.attrs['placeholder'] = self.fields['user_key'].label
        self.fields['user_key'].widget.attrs['max_length'] = 8

    def _set_errors_css(self):
        for field in self:
            if field.errors:
                self._update_cssclass(field.name, 'error')

    def _update_cssclass(self, field_name, css_string):
        if field_name not in self.fields:
            return
        self.fields[field_name].widget.attrs['class'] = \
            (self.fields[field_name].widget.attrs.get('class', '') + ' ' + css_string).strip()

    def clean_user_key(self):
        """ Check user key and get user's """
        user_key = self.data.get('user_key')
        # find guest by this key
        guest = Guest.objects.filter(user_key=user_key).first()

        if not guest:
            raise ValidationError('Не верный код доступа.')

        self.user = authenticate(username=guest.user.username, password=guest.user_key)

        if not self.user:
            raise ValidationError('Не верный код доступа.')

        if not self.user.is_active:
            raise ValidationError('Аккаунт отключен.')
