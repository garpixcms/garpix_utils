from .delete_mixin import DeleteMixin
from .active_mixin import ActiveMixin
from ..managers.available_manager import AvailableManager


class AvailableMixin(ActiveMixin, DeleteMixin):
    available_objects = AvailableManager()

    class Meta:
        abstract = True
