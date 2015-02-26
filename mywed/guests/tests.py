from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from guests.models import Guest
from guests.forms import LoginForm

import http


class GuestModelsTestCase(TestCase):

    """ Test guest model's """

    model = Guest

    def setUp(self):
        self.kwargs = dict(user_key='879987aa')

    def test_guest_verbose_names(self):
        """ Test verbose name for Guest model """
        # create verbose_names dict with correct name of fields
        verbose_names = dict(user='Пользователь', user_key='Код доступа')
        # create counter to check correct number of fields
        counter = 0
        # cycle check verbose names
        for field in verbose_names:
            field = self.model._meta.get_field_by_name(field)[0]
            counter += 1
            self.assertEquals(field.verbose_name, verbose_names[field.name])
        # check is counter has a correct value
        self.assertEquals(counter, 2)
        # check class verbose name
        self.assertEquals(self.model._meta.verbose_name, 'Гость')
        self.assertEquals(self.model._meta.verbose_name_plural, 'Гости')

    def test_guest_save_to_db(self):
        """ Create object and save it to db """
        # check count befor create, correct fxt load
        count = self.model.objects.all().count()
        self.assertEquals(count, 0)
        count = User.objects.all().count()
        self.assertEquals(count, 0)
        # create obect
        instance = self.model(**self.kwargs)
        instance.save()
        # check correct create
        self.assertEquals(self.model.objects.all().count(), count + 1)
        self.assertEquals(User.objects.all().count(), count + 1)
        instance_db = self.model.objects.get(**self.kwargs)
        self.assertEquals(instance, instance_db)
        self.assertEquals(instance.user_key, instance.user.username)

    def test_guest_change_user_key(self):
        """ Change guest user_key - change user user_key """
        instance = self.model(**self.kwargs)
        instance.save()
        self.assertEquals(instance.user_key, instance.user.username)
        # change user key
        instance.user_key = '77777777'
        instance.save()
        self.assertEquals(self.kwargs['user_key'], instance.user.username)
        self.assertEquals(instance.user_key, '77777777')

    def test_guest_wrong_userkey(self):
        """ Check error message if wrong user_key """
        instance = self.model(user_key='999999999999999999999999999')
        self.assertRaises(ValidationError, instance.full_clean)
        instance = self.model(user_key='$@#@#$$#')
        self.assertRaises(ValidationError, instance.full_clean)
        instance = self.model(user_key='1234567')
        self.assertRaises(ValidationError, instance.full_clean)


class GuestFormsTestCase(TestCase):

    """ Test guest form's """

    form_class = LoginForm

    def setUp(self):
        self.form = self.form_class()
        self.fields = self.form.fields

    def test_labels(self):
        """ Test fields labels """
        valid_labels = dict(user_key='Код доступа', )
        for name, label in valid_labels.items():
            self.assertEqual(self.fields.get(name).label, label)

    def test_availability_fields(self):
        """ Test availability fields  """
        available_fields = ('user_key', )
        for name, field in self.fields.items():
            self.assertIn(name, available_fields)

    def test_required_fields(self):
        """ Check field requirement """
        for name in ('user_key', ):
            self.assertTrue(self.form.fields[name].required)

    def test_user_key_validation(self):
        """ Test validation user_key """
        # create user and disabled it
        guest = Guest.objects.create(user_key='12345678')
        guest.user.is_active = False
        guest.user.save()
        # check validation errors
        form = self.form_class(data=dict())
        self.assertIn('Обязательное поле.', form.errors.get('user_key')[0])
        form = self.form_class(data=dict(user_key='asdffdasdfa'))
        self.assertIn('Не верный код доступа.', form.errors.get('user_key')[0])
        form = self.form_class(data=dict(user_key='12345678'))
        self.assertIn('Аккаунт отключен.', form.errors.get('user_key')[0])
        # correct validate
        guest.user.is_active = True
        guest.user.save()
        form = self.form_class(data=dict(user_key='12345678'))
        self.assertTrue(form.errors.get('user_key') is None)


class GuestViewsTestCase(TestCase):

    """ Test guest view's """

    def setUp(self):
        # create guest
        self.kwargs = dict(user_key='12345678')
        self.login_url = reverse('login')
        Guest.objects.create(**self.kwargs)

    def test_guest_200(self):
        """ Test open login page """
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, http.client.OK)

    def test_guest_login(self):
        """ Test login user """
        response = self.client.post(self.login_url, data=self.kwargs)
        self.assertEquals(response.status_code, http.client.FOUND)
