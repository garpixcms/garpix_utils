from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import LazyObject
from django.shortcuts import get_object_or_404
from django.contrib.sites.models import Site
from django.core.cache import cache
from django.conf import settings

HOST_SITE_TIMEOUT = getattr(settings, 'HOST_SITE_TIMEOUT', 3600)


class LazySite(LazyObject):

    def __init__(self, request, *args, **kwargs):
        super().__init__()
        self.__dict__.update({
            'name': request.get_host(),
            'args': args,
            'kwargs': kwargs,
        })

    def _setup(self):
        host = self.name
        site = get_object_or_404(Site, domain__iexact=host)
        self._wrapped = site


class CachedLazySite(LazySite):

    def _setup(self):
        host = self.name
        cache_key = "hosts:%s" % host
        site = cache.get(cache_key, None)
        if site is not None:
            self._wrapped = site
            return
        site = get_object_or_404(Site, domain__iexact=host)
        cache.set(cache_key, site, HOST_SITE_TIMEOUT)
        self._wrapped = site


class CurrentDomainMiddleware(MiddlewareMixin):
    def process_request(self, request, *args, **kwargs):
        request.site = CachedLazySite(request, *args, **kwargs)
