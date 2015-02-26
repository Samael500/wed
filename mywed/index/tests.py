from django.test import TestCase
from django.core.urlresolvers import reverse
from guests.models import Guest

import http


class GuestViewsTestCase(TestCase):

    """ Test guest view's """

    def login_guests(self):
        """ Login user guest """
        response = self.client.post(self.login_url, data=self.kwargs)
        self.assertEquals(response.status_code, http.client.FOUND)

    def setUp(self):
        # create guest
        self.kwargs = dict(user_key='12345678')
        self.login_url = reverse('login')
        self.index_url = reverse('index')
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
