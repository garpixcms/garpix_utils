from django.db import models


class EmptyMixin(models.Model):
    class Meta:
        abstract = True
