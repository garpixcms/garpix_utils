from polymorphic.managers import PolymorphicManager


class PolymorphicAvailableManager(PolymorphicManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, is_deleted=False)
