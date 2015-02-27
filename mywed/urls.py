from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin

from guests.views import LoginFormView
from index.views import IndexView
from news.views import NewsListView, NewsDetailView


urlpatterns = patterns(
    '',

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login$', LoginFormView.as_view(), name='login'),
    url(r'^$', login_required(IndexView.as_view()), name='index'),
    url(r'^news$', login_required(NewsListView.as_view()), name='news'),
    url(r'^news/(?P<pk>\d+)$', login_required(NewsDetailView.as_view()), name='news_detail'),
)
