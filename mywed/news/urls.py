from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from news import views


urlpatterns = patterns(
    '',
    url(r'^$', login_required(views.NewsListView.as_view()), name='news'),
    url(r'^/(?P<pk>\d+)$', login_required(views.NewsDetailView.as_view()), name='news_detail'),
)
