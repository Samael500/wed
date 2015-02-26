from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
import index.views as views


urlpatterns = patterns(
    '',
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
)
