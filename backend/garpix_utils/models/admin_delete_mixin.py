from django.contrib import admin


class AdminDeleteMixin(admin.ModelAdmin):
    class Meta:
        abstract = True

    def delete_queryset(self, request, queryset):
        for item in queryset:
            item.is_deleted = True
            item.save()

    actions = (
        'hard_delete_queryset',
    )

    def hard_delete_queryset(self, request, queryset):
        for item in queryset:
            item.hard_delete()

    hard_delete_queryset.short_description = 'Удалить из базы данных'
