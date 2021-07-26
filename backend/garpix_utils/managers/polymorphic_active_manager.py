from polymorphic.managers import PolymorphicManager


class PolymorphicActiveManager(PolymorphicManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
