from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models
from django.utils.translation import gettext_lazy as _


class BaseFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content_size_mb', 'extension')
    exclude = ('size',)
    readonly_fields = ('id', 'name', 'content_size_mb', 'extension', 'created_at')
    list_filter = ('extension', )
    search_fields = ('id', 'name', 'content')

    def content_size_mb(self, obj):
        if obj:
            return "%.2f MB" % ((obj.size or 0) / 1024 / 1024)
        return '-'

    content_size_mb.admin_order_field = 'size'
    content_size_mb.short_description = _("File size (MB)")

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(models.File)
class FileAdmin(BaseFileAdmin):

    def download(self, obj):
        return mark_safe('<a href="%s" target="_blank"><i class="center fas fa-download"></i><a>' % (obj.content.url,))

    download.short_description = _("Download")

    def get_list_display(self, request):
        return self.list_display + ('download',)

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + ('download',)


@admin.register(models.Image)
class ImageAdmin(BaseFileAdmin):

    def img_preview(self, obj):
        return mark_safe('<a href="%s"><img src="%s" width="70" height="70" /><a>' % (obj.content.url, obj.content.url))

    img_preview.short_description = _("Preview")

    def get_list_display(self, request):
        return self.list_display + ('img_preview',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('img_preview',)
        return self.readonly_fields
