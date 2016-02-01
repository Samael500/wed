from django.views.generic import ListView, DetailView
from helpers.pagination import CustomPaginationMixin
from news.models import News
from django.conf import settings


class NewsListView(CustomPaginationMixin, ListView):

    """ News view class """

    model = News
    template_name = 'news.html'
    # paginate_by = settings.PAGINATE_BY


class NewsDetailView(DetailView):

    """ News detail view class """

    model = News
    template_name = 'news_detail.html'
