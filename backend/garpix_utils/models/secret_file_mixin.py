from django.db import models
from garpix_utils.file.file_field import UploadTo, secret_file_storage
from garpix_utils.string import GenerateHash


class SecretFileMixin(models.Model):
    file = models.FileField(verbose_name='Файл', upload_to=UploadTo('file'), storage=secret_file_storage)
    share_hash = models.CharField(max_length=32, null=True, default=GenerateHash(32), blank=True)

    class Meta:
        abstract = True
