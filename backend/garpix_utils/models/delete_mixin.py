from django.db import models


class DeleteMixin(models.Model):
    is_deleted = models.BooleanField(default=False, verbose_name='Запись удалена')

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def hard_delete(self):
        super(DeleteMixin, self).delete()
