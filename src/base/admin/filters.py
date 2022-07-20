from django.contrib.admin import SimpleListFilter
from django.utils.translation import gettext_lazy as _


class NullListFilter(SimpleListFilter):
    parameter_name = None  # field name
    title = None  # display name

    def lookups(self, request, model_admin):
        return (
            ('0', _('Null')),
            ('1', _('Not null'))
        )

    def queryset(self, request, queryset):
        if self.value() in ('0', '1'):
            kwargs = {'{0}__isnull'.format(self.parameter_name): self.value() == '0'}
            return queryset.filter(**kwargs)
        return queryset
