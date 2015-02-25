from django.contrib import admin
from guests.models import Guest


class GuestAdmin(admin.ModelAdmin):

    """ Admin guest class """

    pass


admin.site.register(Guest, GuestAdmin)
