from django.contrib.sites.models import Site
from django.db import models
from django.db.models import Manager

from garpix_utils.managers import GCurrentSiteManager
from django.core.cache import cache


class GarpixSiteConfiguration(models.Model):
    cache_name = 'garpix_site_config'

    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    objects = Manager()
    on_site = GCurrentSiteManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_to_cache()

    def delete(self, *args, **kwargs):
        self.clear_cache()
        super().delete(*args, **kwargs)

    @classmethod
    def clear_cache(cls):
        cache.delete(cls.get_cache_key())

    def set_to_cache(self):
        cache.set(self.get_cache_key(), self)

    @classmethod
    def get_cache_key(cls):
        current_site = Site.objects.get_current()
        return f'{cls.cache_name}_{current_site.pk}'

    @classmethod
    def get_solo(cls):

        obj = cache.get(cls.get_cache_key())
        if not obj:
            current_site = Site.objects.get_current()
            obj = cls.objects.filter(site=current_site).first() or cls.objects.create(site=current_site)
            obj.set_to_cache()
        return obj

    def __str__(self):
        return f'Настройки для сайта {self.site.name}'

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайтов'
        abstract = True
