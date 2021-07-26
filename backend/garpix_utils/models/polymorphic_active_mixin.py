from django.db import models
from polymorphic_tree.models import PolymorphicMPTTModel
from ..managers.polymorphic_active_manager import PolymorphicActiveManager


class PolymorphicActiveMixin(PolymorphicMPTTModel):
    is_active = models.BooleanField(default=True, verbose_name='Включено')
    active_objects = PolymorphicActiveManager()

    class Meta:
        abstract = True
