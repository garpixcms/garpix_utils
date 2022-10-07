from django.contrib import admin
from django.contrib.sites.models import Site


class GarpixSiteConfigurationAdmin(admin.ModelAdmin):
    exclude = ('site',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        ModelClass = self.model
        lines = ModelClass.objects.all().values_list('site', flat=True)
        sites = Site.objects.exclude(id__in=lines)
        for site in sites:
            ModelClass.objects.create(site=site)
        return super().get_queryset(request)
