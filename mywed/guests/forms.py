from django import forms
from django.core.exceptions import ValidationError
from guests.models import Guest


class LoginForm(forms.Form):

    """ Form for login guests """

    user_key = forms.CharField(required=True)

    def clean_user_key(self):
        """ Check user key and get user's """
        user_key = self.data.get('user_key')
        # find guest by this key
        guest = Guest.objects.filter(user_key=user_key).first()
        if not guest:
            raise ValidationError('Не верный код доступа.')
