from django.contrib import admin

from garpix_utils.cef_logs.mixins.create_log import CreateLogMixin


class LogAdminMixin(admin.ModelAdmin, CreateLogMixin):
    class Meta:
        abstract = True

    def save_model(self, request, obj, form, change):
        events = self.logs_change_or_create(request, obj, change)
        super().save_model(request, obj, form, change)
        for event in events:
            event()

    def save_related(self, request, form, formsets, change):
        if change:
            events = self.logs_change_m2m_field(
                request, super(), form, formsets, change
            )
            for event in events:
                event()
        else:
            super().save_related(request, form, formsets, change)

    def delete_model(self, request, obj):
        event = self.log_delete(request, obj)
        super().delete_model(request, obj)
        event()

    def delete_queryset(self, request, queryset):
        events = []
        for obj in queryset:
            events.append(self.log_delete(request, obj))
        super().delete_queryset(request, queryset)
        for event in events:
            event()
