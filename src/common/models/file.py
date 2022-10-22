from datetime import datetime

from django.db import models
from django.utils.crypto import get_random_string

from django.utils.translation import gettext_lazy as _


def file_path_generator(instance, filename):
    unique_id = get_random_string(length=32)
    if '.' in instance.content.name:
        fl = instance.content.name.split('.')  # to get file extension
        instance.name = instance.content.name
        instance.extension = fl[-1]
        instance.content.name = unique_id + '.' + fl[-1]
        print('in')
    else:
        instance.name = instance.content.name
        instance.content.name = unique_id
    instance.size = instance.content.size
    year, month, day = datetime.now().strftime("%Y/%m/%d").split('/')
    return "{}/{}/{}/{}/{}".format('files', year, month, day, unique_id)


class BaseFile(models.Model):
    content = None  # child classes must define this as a FileField subclass instance
    size = models.IntegerField(verbose_name=_("Size"),
                               null=True, blank=True, help_text=_("Size of file in bytes"))
    name = models.CharField(verbose_name=_("Name"), max_length=1024, blank=True)
    extension = models.CharField(verbose_name=_("Extension"), max_length=255, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))

    def save(self, *args, **kwargs):
        if '.' in self.content.name:
            fl = self.content.name.split('.')  # to get file extension
            self.name = self.content.name
            self.extension = fl[-1]
        else:
            self.name = self.content.name
        self.size = self.content.size
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return "%s" % self.content

    class Meta:
        abstract = True


class Image(BaseFile):
    content = models.ImageField(verbose_name=_("Image"), upload_to=file_path_generator)

    class Meta:
        app_label = 'panel_files'
        db_table = "common_image"
        verbose_name = _("Image")
        verbose_name_plural = _("Images")
        ordering = ('-id',)


class File(BaseFile):
    content = models.FileField(verbose_name=_("File"), upload_to=file_path_generator)

    class Meta:
        app_label = 'panel_files'
        db_table = "file"
        verbose_name = _("File")
        verbose_name_plural = _("Files")
        ordering = ('-id',)
