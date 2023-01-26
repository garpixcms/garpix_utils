from garpix_utils.managers import GCurrentSiteManager


class ActiveOnSiteManager(GCurrentSiteManager):

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
