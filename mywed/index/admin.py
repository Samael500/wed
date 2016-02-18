from django import forms
from django.contrib import admin
from django_summernote.widgets import SummernoteWidget
from django_summernote.admin import AttachmentAdmin, Attachment
from index.models import WebPage, Carousel


class WebPageAdminForm(forms.ModelForm):

    """ Form with SummernoteWidget """

    class Meta:
        model = WebPage
        exclude = ('pk', )
        # widgets = {'content': SummernoteWidget(), }


class WebPageAdmin(admin.ModelAdmin):

    """ WebPage news class """

    list_display = ('kind', 'title', )
    readonly_fields = ('created_at', 'modified_at')

    form = WebPageAdminForm


class CarouselAdmin(admin.ModelAdmin):

    """ Carousel andim class """

    list_display = ('__str__', )


class CustomAttachmentAdmin(AttachmentAdmin):

    def get_model_perms(self, request):
        return dict()


admin.site.unregister(Attachment)
admin.site.register(WebPage, WebPageAdmin)
admin.site.register(Attachment, CustomAttachmentAdmin)
admin.site.register(Carousel, CarouselAdmin)
