from django.test import TestCase
from django.core.urlresolvers import reverse
from guests.models import Guest
from index.models import WebPage

import http


class WebPageModelsTestCase(TestCase):

    """ Test web page model's """

    model = WebPage

    def setUp(self):
        self.kwargs = dict(kind=WebPage.INDEX, title='test text', content='2015-03-08')

    def test_webpage_verbose_names(self):
        """ Test verbose name for Guest model """
        # create verbose_names dict with correct name of fields
        verbose_names = dict(
            kind='Тип страницы', title='Заголовок', content='Содержание страницы',
            created_at='Время создания', modified_at='Время последнего изменения', )
        # create counter to check correct number of fields
        counter = 0
        # cycle check verbose names
        for field in verbose_names:
            field = self.model._meta.get_field_by_name(field)[0]
            counter += 1
            self.assertEquals(field.verbose_name, verbose_names[field.name])
        # check is counter has a correct value
        self.assertEquals(counter, 5)
        # check class verbose name
        self.assertEquals(self.model._meta.verbose_name, 'Страница')
        self.assertEquals(self.model._meta.verbose_name_plural, 'Страницы')

    def test_webpage_save_to_db(self):
        """ Create object and save it to db """
        # check count befor create, correct fxt load
        count = self.model.objects.all().count()
        self.assertEquals(count, 0)
        # create obect
        instance = self.model(**self.kwargs)
        instance.save()
        # check correct create
        self.assertEquals(self.model.objects.all().count(), count + 1)
        instance_db = self.model.objects.get(**self.kwargs)
        self.assertEquals(instance, instance_db)
        # check str
        self.assertEquals('Главная страница: test text', str(instance))


class IndexViewsTestCase(TestCase):

    """ Test index view's """

    def login_guests(self):
        """ Login user guest """
        response = self.client.post(self.login_url, data=self.kwargs)
        self.assertEquals(response.status_code, http.client.FOUND)

    def setUp(self):
        # create guest
        self.kwargs = dict(user_key='12345678')
        self.login_url = reverse('login')
        self.index_url = reverse('index')
        self.contacts_url = reverse('contacts')
        Guest.objects.create(**self.kwargs)

    def test_index_200(self):
        """ Test open index page """
        self.login_guests()
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, http.client.OK)

    def test_index_redirect(self):
        """ Test redirect to login user """
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, http.client.FOUND)
        self.assertRedirects(response, self.login_url + '?next=/')

    def test_index_contacts_hase_content(self):
        """ Check pages correct show'd """
        wbp_index = WebPage.objects.create(kind=WebPage.INDEX, title='test index', content='test content index')
        wbp_cont = WebPage.objects.create(kind=WebPage.CONTACTS, title='test contacts', content='test content cont')
        self.login_guests()
        # check index
        response = self.client.get(self.index_url)
        str_response = str(response.content.decode('utf-8'))
        self.assertIn(wbp_index.title, str_response)
        self.assertIn(wbp_index.content, str_response)
        self.assertNotIn(wbp_cont.title, str_response)
        self.assertNotIn(wbp_cont.content, str_response)
        # check contacts
        response = self.client.get(self.contacts_url)
        str_response = str(response.content.decode('utf-8'))
        self.assertNotIn(wbp_index.title, str_response)
        self.assertNotIn(wbp_index.content, str_response)
        self.assertIn(wbp_cont.title, str_response)
        self.assertIn(wbp_cont.content, str_response)

    def test_contacts_200(self):
        """ Test open contacts page """
        self.login_guests()
        response = self.client.get(self.contacts_url)
        self.assertEquals(response.status_code, http.client.OK)

    def test_contacts_redirect(self):
        """ Test redirect to login user """
        response = self.client.get(self.contacts_url)
        self.assertEquals(response.status_code, http.client.FOUND)
        self.assertRedirects(response, self.login_url + '?next=/contacts')
