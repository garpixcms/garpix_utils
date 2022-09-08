from django.conf import settings
from django.contrib.sites.managers import CurrentSiteManager
from polymorphic_tree.managers import PolymorphicMPTTModelManager


class GPolymorphicCurrentSiteManager(CurrentSiteManager, PolymorphicMPTTModelManager):
    use_in_migrations = False

    def get_queryset(self):
        qs = self.queryset_class(self.model, using=self._db, hints=self._hints)
        if self.model._meta.proxy:
            qs = qs.instance_of(self.model)
        return qs.filter(**{self._get_field_name() + '__id': getattr(settings, 'SITE_ID', 1)})
