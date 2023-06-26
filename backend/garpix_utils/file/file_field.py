import datetime
import os

import uuslug
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def get_file_path(instance, filename):
    """
    Формирует путь файла относительно года и месяца, чтобы множество файлов не скапливались на одном уровне.
    """
    ext = filename.split('.')[-1]
    today = datetime.date.today()
    filename = f'{uuslug.slugify(".".join(filename.split(".")[:-1]))}.{ext}'
    return f'uploads/{today.year}/{today.month}/{filename}'


class UploadTo:

    def __init__(self, field_name):
        self.field_name = field_name

    def __call__(self, instance, filename):
        """
        Формирует путь файла относительно названия модели, поля, года и месяца, чтобы множество файлов
        не скапливались на одном уровне.
        """
        ext = filename.split('.')[-1]
        today = datetime.date.today()
        filename = f'{uuslug.slugify(".".join(filename.split(".")[:-1]))}.{ext}'
        return f'uploads/{instance.__class__.__name__}/{self.field_name}/{today.year}/{today.month}/{filename}'

    def deconstruct(self):
        return ('garpix_utils.file.UploadTo', [self.field_name], {})


def secret_file_storage():
    fs = FileSystemStorage(location=getattr(settings, 'SECRET_MEDIA_ROOT',
                                            os.path.join(settings.BASE_DIR, '..', 'secret_public', 'media')))
    return fs
