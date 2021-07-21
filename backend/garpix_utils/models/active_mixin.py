from django.db import models
from ..managers.active_manager import ActiveManager


class ActiveMixin(models.Model):
    is_active = models.BooleanField(default=True, verbose_name='Включено')
    objects = models.Manager()
    active_objects = ActiveManager()

    class Meta:
        abstract = True
