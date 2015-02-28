from django.http.response import Http404
from pure_pagination import PaginationMixin, EmptyPage
from pure_pagination.paginator import Page, add_page_querystring, Paginator


class CustomPage(Page):

    """
    Custom Page class for pure_pagination app
    Add first and last page with querystring
    """

    @add_page_querystring
    def first_page_number(self):
        return 1

    @add_page_querystring
    def last_page_number(self):
        return max(self.paginator.num_pages, 1)


class CustomPaginator(Paginator):

    """ Custom Paginator with override page method """

    def page(self, number):
        """ Returns a CustomPage object for the given 1-based page number. """
        number = self.validate_number(number)
        bottom = (number - 1) * self.per_page
        top = bottom + self.per_page
        if top + self.orphans >= self.count:
            top = self.count
        return CustomPage(self.object_list[bottom:top], number, self)


class CustomPaginationMixin(PaginationMixin):

    """ Override pagination_class in PaginationMixin """

    paginator_class = CustomPaginator

    def paginate_queryset(self, *args, **kwargs):
        """ Throw 404 Exception if there is no existing page by default """
        try:
            return super().paginate_queryset(*args, **kwargs)
        except EmptyPage:
            raise Http404
