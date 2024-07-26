from django.contrib import admin


class HideableFieldsMixin(admin.ModelAdmin):
    class Media:
        js = (
            'garpix_utils/admin/js/hideable_fields.js',
        )
