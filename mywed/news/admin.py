from django.contrib import admin
from news.models import News


class NewsAdmin(admin.ModelAdmin):

    """ Admin news class """

    list_display = ('pub_date', 'title', )
    readonly_fields = ('created_at', 'modified_at')


admin.site.register(News, NewsAdmin)
