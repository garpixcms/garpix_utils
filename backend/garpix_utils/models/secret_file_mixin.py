from django.db import models
from garpix_utils.file.file_field import UploadTo, secret_file_storage
from garpix_utils.string import get_uuid4_hash


class SecretFileMixin(models.Model):
    file = models.FileField(verbose_name='Файл', upload_to=UploadTo('file'), storage=secret_file_storage)
    share_hash = models.CharField(max_length=32, null=True, default=get_uuid4_hash(), blank=True)

    class Meta:
        abstract = True
