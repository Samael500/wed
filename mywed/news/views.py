from django.views.generic import TemplateView


class NewsListView(TemplateView):

    """ News view class """

    template_name = 'news.html'
