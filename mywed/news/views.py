from django.views.generic import ListView, DetailView
from news.models import News


class NewsListView(ListView):

    """ News view class """

    model = News
    template_name = 'news.html'


class NewsDetailView(DetailView):

    """ News detail view class """

    model = News
    template_name = 'news_detail.html'
