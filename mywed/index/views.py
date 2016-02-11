from django.views.generic import TemplateView, ListView
from index.models import WebPage, Carousel


class IndexView(TemplateView):

    """ Index view class """

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(dict(index_page=WebPage.objects.filter(kind=WebPage.INDEX).first()))
        return context


class ContactsView(TemplateView):

    """ Contacts view class """

    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(dict(contacts_page=WebPage.objects.filter(kind=WebPage.CONTACTS).first()))
        return context


class ImageGallery(ListView):

    """ Display image gallery """

    template_name = 'gallery.html'

    model = Carousel
