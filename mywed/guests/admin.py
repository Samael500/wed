from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as SuperUserAdmin
from guests.models import Guest


class GuestAdmin(admin.ModelAdmin):

    """ Admin guest class """

    list_display = ('get_first_name', 'get_last_name', 'user_key', )

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'Имя'
    get_first_name.admin_order_field = 'user__username'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Фамилия'
    get_last_name.admin_order_field = 'user__last_name'


class GuestAdminInline(admin.TabularInline):

    """ Guest inline to user """

    model = Guest
    max_num = 1
    extra = 0


class UserAdmin(SuperUserAdmin):

    """ Custom user admin class """

    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_guest', 'has_enter')

    def get_fieldsets(self, request, obj=None):
        fieldsets = list(self.fieldsets)
        fieldsets[2] = ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser')})
        return fieldsets

    inlines = (GuestAdminInline, )

    def is_guest(self, obj):
        return hasattr(obj, 'guest_profile')
    is_guest.short_description = u'статус гостя'
    is_guest.boolean = True

    def has_enter(self, obj):
        return obj.last_login > obj.date_joined
    has_enter.short_description = u'Заходил'
    has_enter.boolean = True


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Guest, GuestAdmin)
admin.site.register(User, UserAdmin)
