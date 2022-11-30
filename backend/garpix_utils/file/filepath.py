import uuslug
from garpix_utils.string import get_random_string
import datetime
import os
from django.conf import settings


def get_secret_path(filename=None):
    today = datetime.date.today()
    subdir1 = get_random_string(16)
    subdir2 = get_random_string(16)
    subdir3 = get_random_string(16)
    path = 'data/%s/%s/%s/%s/%s' % (today.year, today.month, subdir1, subdir2, subdir3)
    os.makedirs(os.path.join(settings.MEDIA_ROOT, path))
    if filename is None:
        return path

    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuslug.slugify(".".join(filename.split('.')[:-1])), ext)

    return os.path.join(path, filename)
