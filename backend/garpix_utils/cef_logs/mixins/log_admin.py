from django.contrib import admin

from garpix_utils.cef_logs.mixins.create_log import CreateLogMixin


class LogAdminMixin(admin.ModelAdmin, CreateLogMixin):
    class Meta:
        abstract = True

    def save_model(self, request, obj, form, change):
        events = self.logs_change_or_create(request, obj, change)
        super().save_model(request, obj, form, change)
        for event, args in events:
            event(**args)

    def save_related(self, request, form, formsets, change):
        if change:
            events = self.logs_change_m2m_field(
                request, super(), form, formsets, change
            )
            if events:
                for event, args in events:
                    event(**args)
        else:
            super().save_related(request, form, formsets, change)

    def delete_model(self, request, obj):
        event, args = self.log_delete(request, obj)
        super().delete_model(request, obj)
        event(**args)

    def delete_queryset(self, request, queryset):
        events = []
        for obj in queryset:
            events.append(self.log_delete(request, obj))
        super().delete_queryset(request, queryset)
        for event, args in events:
            event(**args)
