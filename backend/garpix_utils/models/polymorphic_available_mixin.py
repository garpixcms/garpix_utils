from .delete_mixin import DeleteMixin
from .active_mixin import ActiveMixin
from polymorphic_tree.models import PolymorphicMPTTModel
from ..managers.polymorphic_available_manager import PolymorphicAvailableManager


class PolymorphicAvailableMixin(ActiveMixin, DeleteMixin, PolymorphicMPTTModel):
    available_objects = PolymorphicAvailableManager()

    class Meta:
        abstract = True
