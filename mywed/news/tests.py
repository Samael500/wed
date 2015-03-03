from django.test import TestCase
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.conf import settings
from guests.models import Guest
from news.models import News

import http


class NewsModelsTestCase(TestCase):

    """ Test news model's """

    model = News

    def setUp(self):
        self.kwargs = dict(title='test title', text='test text', pub_date='2015-03-08')

    def test_news_verbose_names(self):
        """ Test verbose name for Guest model """
        # create verbose_names dict with correct name of fields
        verbose_names = dict(
            title='Заголовок', text='Содержание новости', pub_date='Дата публикации',
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
        self.assertEquals(self.model._meta.verbose_name, 'Новость')
        self.assertEquals(self.model._meta.verbose_name_plural, 'Новости')

    def test_news_save_to_db(self):
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
        self.assertEquals('2015-03-08: test title', str(instance))

    def test_news_wrong_userkey(self):
        """ Check error message ValidationError """
        # no title
        kwargs = self.kwargs.copy()
        kwargs.pop('title')
        instance = self.model(**kwargs)
        self.assertRaises(ValidationError, instance.full_clean)
        # no text
        kwargs = self.kwargs.copy()
        kwargs.pop('text')
        instance = self.model(**kwargs)
        self.assertRaises(ValidationError, instance.full_clean)


class NewsViewsTestCase(TestCase):

    """ Test news view's """

    def login_guests(self):
        """ Login user guest """
        Guest.objects.create(**self.login_kwargs)
        response = self.client.post(self.login_url, data=self.login_kwargs)
        self.assertEquals(response.status_code, http.client.FOUND)

    def setUp(self):
        # create guest
        self.kwargs = dict(title='test title', text='test text', pub_date='2015-03-08')
        self.new = News.objects.create(**self.kwargs)
        self.login_kwargs = dict(user_key='12345678')
        self.login_url = reverse('login')
        self.news_url = reverse('news')
        self.news_item_url = reverse('news_detail', kwargs=dict(pk=self.new.pk, ))

    def test_news_200(self):
        """ Test open news page """
        self.login_guests()
        response = self.client.get(self.news_url)
        self.assertEquals(response.status_code, http.client.OK)

    def test_news_redirect(self):
        """ Test redirect to login user """
        response = self.client.get(self.news_url)
        self.assertEquals(response.status_code, http.client.FOUND)
        self.assertRedirects(response, self.login_url + '?next=/news/')

    def test_news_item_200(self):
        """ Test open news page """
        self.login_guests()
        response = self.client.get(self.news_item_url)
        self.assertEquals(response.status_code, http.client.OK)
        # check has correct values in response
        str_content = response.content.decode('utf-8')
        self.assertIn(self.kwargs['title'], str_content)
        self.assertIn(self.kwargs['text'], str_content)

    def test_news_item_redirect(self):
        """ Test redirect to login user """
        response = self.client.get(self.news_item_url)
        self.assertEquals(response.status_code, http.client.FOUND)
        self.assertRedirects(response, self.login_url + '?next=/news/%d' % self.new.pk)

    def test_news_paginate(self):
        """ Test correct paginate """
        # change pagination settings
        from news.views import NewsListView
        NewsListView.paginate_by = 1
        # login user
        self.login_guests()
        News.objects.create(**self.kwargs)
        News.objects.create(**self.kwargs)
        # check count correct
        self.assertEquals(News.objects.all().count(), 3)
        # check request
        response = self.client.get(self.news_url)
        self.assertEquals('<Page 1 of 3>', str(response.context_data['page_obj']))
