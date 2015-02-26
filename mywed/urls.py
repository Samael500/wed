from django.conf.urls import patterns, include, url
from django.contrib import admin
from guests.views import LoginFormView

urlpatterns = patterns(
    '',

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login$', LoginFormView.as_view(), name='login'),
    url(r'^', include('index.urls')),
)
