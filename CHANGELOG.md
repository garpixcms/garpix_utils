### 1.9.0-rc1 (26.06.2023)

- [DEPRECETED] get_file_path
- Добавлен класс `UploadTo` - замена функции `get_file_path` (генерирует путь с учетом названия модели и поля)
- Добавлен класс `GenerateHash` - создание строки случайных символов (для CharField)
- Добавлена функция `secret_file_storage` - получение хранилища скрытых файлов (для FileField)
- Добавлены миксины `SecretFileMixin`, `SecretFileViewMixin`, `SecretFileSerializerMixin` для моделей, вью и сериалайзеров соответственно - работа со скрытыми файлами (см. `Readme.md`)

### 1.8.0 (26.01.2023)

- Добавлен менеджер `ActiveOnSiteManager`

### 1.7.0 (22.11.2022)

- Добавлена функция генерации уникального пути файла (`file.get_secret_path`)

### 1.6.0 (07.10.2022)

- Добавлен класс для добавления мультисайтовых настроек `GarpixSiteConfiguration`

### 1.5.1 (07.09.2022)

- Поправлен баг: `'Settings' object has no attribute 'getattr'`

### 1.5.0 (29.07.2022)

- Добавлены менеджеры `GCurrentSiteManager`, `GPolymorphicCurrentSiteManager`.

### 1.4.0 (14.09.2021)

- Добавлен `GarpixPaginator`.

### 1.3.0 (08.09.2021)

- Добавлен AdminDeleteMixin.

### 1.2.0 (08.09.2021)

- Добавлен template tag `url_replace`.

### 1.1.0 (22.07.2021)

- Добавлены `models.EmptyMixin`, `models.PolymorphicActiveMixin`, `managers.PolymorphicActiveManager`
  , `models.AvailableMixin`.

### 1.0.2 (21.07.2021)

- Убран `objects` из ActiveMixin.

### 1.0.1 (21.07.2021)

- Исправлена ошибка с неправильной зависимостью.

### 1.0.0 (21.07.2021)

- Первый релиз на pypi.org
