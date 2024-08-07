# Garpix Utils

Набор утилит для GARPIX CMS.

Утилиты:

* `file.get_file_path` - генерация пути для сохранения файла (для FileField) [DEPRECATED]
* `file.UploadTo` - генерация пути для сохранения файла (для FileField)
* `string.get_random_string` - создание строки случайных символов
* `string.GenerateHash` - создание строки случайных символов (для CharField)
* `signature.make_signature_sha512` - создание цифровой подписи
* `models.ActiveMixin` - миксин для моделей, которым необходимо поле "Активность"
* `models.EmptyMixin` - миксин-пустышка, который можно использовать при обязательных миксинах
* `models.AvailableMixin` - миксин для моделей, которые должны обладать полями "Активность" и "Удалено"
* `models.PolymorphicActiveMixin` - миксин для модели `garpix_page.BasePage`, добавляет возможность выбора доступных
  страниц (которые активны). Используется внутри GARPIX CMS.
* `templatetags.url_replace` - подмена одного значения в dict на другое в Django-шаблонах.
* `models.DeleteMixin` - миксин для моделей, добавляющий функционал мягкого/жесткого удаления, `models.AdminDeleteMixin`
  - миксин для админ.модели.
* `models.PolymorphicAvailableMixin` - миксин для модели `garpix_page.BasePage`, добавляет возможность выбора доступных
  страниц (которые активны и неудалены). Используется внутри GARPIX CMS.
* `models.GarpixSiteConfiguration` - класс для добавления мультисайтовых настроек в
  проекте, `admin.GarpixSiteConfigurationAdmin` - класс для админ.панели
* `string.secret_file_storage` - получение хранилища скрытых файлов (для FileField)
* `models.SecretFileMixin` - миксин для моделей, работа со скрытыми файлами
* `views.SecretFileViewMixin` - миксин для drf viewset, работа со скрытыми файлами
* `serializers.SecretFileSerializerMixin` - миксин для drf serializer, работа со скрытыми файлами
* `admin.HideableFieldsMixin` - миксин для скрытия полей в зависимости от значения селекта и чекбокса в админ-панели

## Установка

Установка с помощью pip:

```bash
pip install garpix_utils
```

### Утилиты

#### `file.UploadTo` - генерация пути для сохранения файла (для FileField)

Класс, каждый вызов которого формирует путь файла относительно названия модели, поля года и месяца, чтобы множество
файлов не скапливались на одном уровне.

Можно использовать в качестве значения 'UploadTo' поля FileField модели Django.

ПРИМЕР:

```
from garpix_utils.file import get_file_path
from django.db import models


class FileModel(models.Model):
    # ...
    file = models.FileField(upload_to=UploadTo('file'), blank=True, null=True, verbose_name=_('File'))
    # ...
```

Параметр 'file' - название поля в пути к файлу.

#### `file.get_file_path` - генерация пути для сохранения файла (для FileField) [DEPRECATED]

Формирует путь файла относительно года и месяца, чтобы множество файлов не скапливались на одном уровне.

Можно использовать в качестве значения 'upload_to' поля FileField модели Django.

ПРИМЕР:

```
from garpix_utils.file import get_file_path
from django.db import models


class FileModel(models.Model):
    # ...
    file = models.FileField(upload_to=get_file_path, blank=True, null=True, verbose_name=_('File'))
    # ...
```

#### `string.get_random_string` - создание строки случайных символов

Создает случайную строку указанного размера и с указанными символами.

Параметры:

* size: int - количество символов. По умолчанию - 8.
* chars: str - строка из списка символов, которые могут быть в строке. По
  умолчанию `string.ascii_uppercase + string.digits`.

ПРИМЕР:

Пример 1

```
from garpix_utils.string import get_random_string

random_string = get_random_string(16)

# random_string = '451DNCLZLY2HDDDX'
```

Пример 2

```
import string
from garpix_utils.string import get_random_string

random_string = get_random_string(8, string.ascii_lowercase)

# random_string = 'palsjpyz'
```

Пример 3

```
from garpix_utils.string import get_random_string

random_string = get_random_string(16, '01')

# random_string = '0110111101010100'
```

### `string.GenerateHash` - создание строки случайных символов (для CharField)

Класс, каждый вызов которого создает случайную строку, используя метод `get_random_string` указанной длины.

Параметры:

* hash_length: int - количество символов. По умолчанию - 32.

Пример:

```
from garpix_utils.file.file_field import UploadTo

class FileModel(models.Model):
    # ...
    share_hash = models.CharField(max_length=32, null=True, default=GenerateHash(32), blank=True)
    # ...
```

#### `signature.make_signature_sha512` - создание цифровой подписи

Создает сигнатуру (цифровую подпись) по указанным параметрам с хэшированием SHA-512.

Обычно используется для эквайринга в качестве защиты цифровой подписью.

ВНИМАНИЕ! Если необходим другой алгоритм шифрования, то загляните в эту функцию, можно сделать свой по аналогии.

Параметры:

* params: dict - словарь параметров. Если присутствует signature_key, то он будет удален.
* signature_key: str - ключ параметра с сигнатурой. По умолчанию "sig".
* secret: str - секретный ключ, который будет приконкатенирован в конце перед хэшированием.

Алгоритм:

1. Берет словарь параметров, удаляет оттуда параметр с ключом сигнатуры (см. переменную signature_key, по умолчанию
   значение "sig")
2. Получившийся словарь сортирует по названию ключа в алфавитном порядке. Все вложенные данные тоже сортируются по
   ключу, списочные - просто по алфавиту.
3. Последовательно конкатенирует ключ со значением в единую строку.
4. В конце конкатенирует значение переменной secret (по умолчанию равна "secret").
5. Хэширует по алгоритму SHA-512 и возвращает строку в нижнем регистре.
6. Возвращает получившийся результат.

ПРИМЕР:

```python
# необходимый вам файл

from garpix_utils.signature import make_signature_sha512

sig = make_signature_sha512(
    {'a': 'xxx', 'c': 'ggg', 'b': '111', 'sig': '123', 'd': [3, 1, 2], 'e': {'b': '2', 'a': '1'}}, signature_key='sig',
    secret='secret')

# sig = '2123086085ec1fe67595d7b3d2b6a0dbf3f33e528d78366b8d62d7f0a7e3c090077b0f7b8dc84921a6087aa57b8284bd1e74702df7a16e96f73f627e6eea815a'
```

Разбор примера по шагам:

**Шаг 1**

* Было: {'a': 'xxx', 'c': 'ggg', 'b': '111', 'sig': '123', 'd': [3, 1, 2], 'e': {'b': '2', 'a': '1'}}
* Стало: {'a': 'xxx', 'c': 'ggg', 'b': '111', 'd': [3, 1, 2], 'e': {'b': '2', 'a': '1'}}

**Шаг 2**

* Было: {'a': 'xxx', 'c': 'ggg', 'b': '111', 'd': [3, 1, 2], 'e': {'b': '2', 'a': '1'}}
* Стало: {'a': 'xxx', 'b': '111', 'c': 'ggg', 'd': [1, 2, 3], 'e': {'a': '1', 'b': '2'}}

**Шаг 3**

* Было: {'a': 'xxx', 'b': '111', 'c': 'ggg', 'd': [1, 2, 3], 'e': {'a': '1', 'b': '2'}}
* Стало: 'axxxb111cgggd123ea1b2'

**Шаг 4**

* Было: 'axxxb111cgggd123ea1b2'
* Стало: 'axxxb111cgggd123ea1b2secret'

**Шаг 5**

* Было: 'axxxb111cgggd123ea1b2secret'
* Стало: '
  2123086085ec1fe67595d7b3d2b6a0dbf3f33e528d78366b8d62d7f0a7e3c090077b0f7b8dc84921a6087aa57b8284bd1e74702df7a16e96f73f627e6eea815a'

#### `models.ActiveMixin` - миксин для моделей, которым необходимо поле "Активность"

Добавляет поле `is_active (Boolean, default=True)`. Добавляет менеджера `active_objects`, который выбирает только
активные объекты (`is_active=True`).

ПРИМЕР:

```python
# необходимый вам файл

from django.db import models
from garpix_utils.models import ActiveMixin


class Product(ActiveMixin, models.Model):
    pass


Product.active_objects.all()

# Будут выбраны записи только с is_active == True.
```

#### `models.EmptyMixin` - миксин-пустышка, который можно использовать при обязательных миксинах

ПРИМЕР:

```python
# необходимый вам файл

from django.db import models
from garpix_utils.models import EmptyMixin


class Product(EmptyMixin, models.Model):
    pass

# Ничего не изменилось.
```

Или использование в пакете `garpix_blog`:

```python
# app/settings.py

GARPIX_BLOG_MIXIN = 'garpix_utils.models.EmptyMixin'

```

#### `models.AvailableMixin` - миксин для моделей, которые должны обладать полями "Активность" и "Удалено"

Добавляет поля `is_active (Boolean, default=True)` и `is_deleted (Boolean, default=False)`. Добавляет
менеджера `available_objects`, который выбирает только доступные объекты (`is_active=True, is_deleted=False`).

ПРИМЕР:

```python
# необходимый вам файл

from django.db import models
from garpix_utils.models import AvailableMixin


class Product(AvailableMixin, models.Model):
    pass


Product.available_objects.all()

# Будут выбраны записи только с is_active == True.
```

#### `templatetags.url_replace` - подмена одного значения в dict на другое в Django-шаблонах.

ПРИМЕР для пагинации (взято из https://github.com/garpixcms/garpix_page/):

```
{% load url_replace %}

<nav>
    <ul class="pagination">
        {% for page_num in page_range %}
            <li class="page-item {% if page_num == page %}active{% endif %}">
                <a class="page-link" href="?{% url_replace request 'page' page_num %}">{{ page_num }}</a>
            </li>
        {% endfor %}
    </ul>
</nav>
```

#### `file.secret_file_storage` - получение хранилища скрытых файлов

Устанавливает хранилище для файлов в поле модели, указанное в настройках `SECRET_MEDIA_ROOT`.

Пример:

Файл настроек:

```python
# settings.py

import os
from app.basedir import BASE_DIR

SECRET_MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'secret_public', 'media')

```

Модель с полем файла:

```python
from garpix_utils.file.file_field import UploadTo, secret_file_storage
from django.db import models


class FileModel(models.Model):
    # ...
    file = models.FileField(upload_to=UploadTo('file'), storage=secret_file_storage)
    # ...
```

#### `models.SecretFileMixin`, `views.SecretFileViewMixin`, `serializers.SecretFileSerializerMixin` - работа со скрытыми файлами

Использование файлов в закрытой папке:

1. Добавить настройку `SECRET_MEDIA_ROOT`:

```python
# settings.py

import os
from app.basedir import BASE_DIR

SECRET_MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'secret_public', 'media')

```

2. Добавить миксин `models.SecretFileMixin` к модели:

```python
from django.db import models
from garpix_utils.models import SecretFileMixin

class Attachment(SecretFileMixin, models.Model):
    # ...
    pass

```

3. Добавить миксин `views.SecretFileViewMixin` к view:

```python
from garpix_utils.views import SecretFileViewMixin
from rest_framework import viewsets
from app.models import Attachment


class AttachmentsView(SecretFileViewMixin, viewsets.GenericViewSet):
    # ...
    queryset = Attachment.objects.all()
    # ...
```

4. Добавить миксин `serializers.SecretFileSerializerMixin` к serializer:

```python
from rest_framework import serializers
from garpix_utils.serializers import SecretFileSerializerMixin


class AttachmentSerializer(SecretFileSerializerMixin, serializers.ModelSerializer):

    view_basename = 'attachments'

    # ...
```

`view_basename` - basename view в url.

#### `admin.HideableFieldsMixin` - миксин для скрытия полей в зависимости от значения селекта и чекбокса в админ-панели

1. В нужную модель подключить этот миксин, а также создать отдельный `.js` файл в проекте и также подключить к этой модели.
```python
class SomeModel(models.Model):
    class SelectTypes(TextChoices):
        VAL1 = 'val1', '1'
        VAL2 = 'val2', '2'
        VAL3 = 'val3', '3'

    my_choices_field = models.CharField(choices=SelectTypes)
    my_bool_field = models.BooleanField()

    field_1 = ...
    field_2 = ...
    field_3 = ...

@admin.register(SomeModel)
class SomeModelAdmin(HideableFieldsMixin):
    class Media:
        js = (
            'admin/js/some_model.js',
        )
```

2. В этом `.js` файле прописать зависимости полей:
```js
// admin/js/some_model.js

window.onload = () => {
    initHideableFields({
        // Объект, где:
        // Ключ - значение поля
        // Значение - массив названий полей в модели, которые будут отображены, в случае выбора этого значения. При этом поля из других значений будут скрыты, если они не перечислены здесь.
        'val1': [],          // При выборе этого значения, поля 'field_1' и 'field_2' будут скрыты.
        'val2': ['field_1'], // Будет показано только поле 'field_1'.
        'val3': [            // Будут показаны оба поля.
            'field_1',
            'field_2',
        ],
    }, 'my_choices_field');  // Название поля с выбором в модели

    initHideableFields({
        'on': [           // Состояние - включено, поле 'field_3' показывается.
            'field_3',
        ],
        'off': [],        // Состояние - выключено, поле 'field_3' не показывается.
    }, 'my_bool_field');  // Название поля с чекбоксом в модели
}
```

# Changelog

See [CHANGELOG.md](CHANGELOG.md).

# Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

# License

[MIT](LICENSE)
