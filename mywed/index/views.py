from django.views.generic import TemplateView


class IndexView(TemplateView):

    """ Index view class """

    template_name = 'base.html'
