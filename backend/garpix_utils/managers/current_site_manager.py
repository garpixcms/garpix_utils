from django.contrib.sites.managers import CurrentSiteManager


class GCurrentSiteManager(CurrentSiteManager):
    use_in_migrations = False
