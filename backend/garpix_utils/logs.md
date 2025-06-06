| ActionType (evenClassId)       | Description                                      |
|--------------------------------|--------------------------------------------------|
| user_account                   | Управление учетными записями пользователей        |
| authentication                 | Идентификация и аутентификация                    |
| user_access_attribute          | Управление атрибутами доступа                     |
| access                         | Доступ к защищаемой информации                    |
| download                       | Загрузка файлов                                  |
| delete                         | Удаление информации                              |
| create                         | Добавление информации                            |
| upload                         | Загрузка информации                              |
| change                         | Изменение информации                             |
| configuration                  | Изменение конфигураций                           |

| Уровень  | Code | ActionType (evenClassId)       | ActionElement Name      | Description                                      |
|----------|------|--------------------------------|-------------------------|--------------------------------------------------|
| Low      | 3    | access                         | Check user existence    | Проверка существования пользователя              |
| Medium   | 4    | authentication                 | System Logout           | Выход из системы                                 |
| Medium   | 6    | authentication                 | System Login            | Вход в систему                                   |
| Medium   | 6    | download                       | Download file           | Загрузка файла                                   |
| Medium   | 6    | user_access_attribute          | Create user group       | Создание группы пользователей                    |
| Medium   | 6    | user_access_attribute          | Change user group       | Изменение группы пользователей                   |
| Medium   | 6    | user_access_attribute          | Add user to group       | Добавление пользователя в группу                 |
| Medium   | 6    | user_access_attribute          | Delete user from group  | Удаление пользователя из группы                  |
| Medium   | 6    | create                         | Create entities         | Создание сущностей                               |
| Medium   | 6    | upload                         | Upload file             | Загрузка файла                                   |
| Medium   | 6    | change                         | Change entities         | Изменение сущностей                              |
| Medium   | 6    | user_account                   | Change user parameters  | Изменение параметров пользователя                |
| High     | 7    | user_access_attribute          | Change user privileges  | Изменение привилегий пользователя                |
| High     | 7    | user_account                   | Registration            | Регистрация пользователя                         |
| High     | 7    | user_account                   | Create user             | Создание нового пользователя                     |
| High     | 8    | user_account                   | Delete user             | Удаление пользователя                            |
| High     | 8    | authentication                 | System Login (Fail)     | Неудачная попытка входа в систему                |
| High     | 8    | user_access_attribute          | Delete user group       | Удаление группы пользователей                    |
| High     | 8    | delete                         | Delete entities         | Удаление сущностей                               |
| High     | 8    | configuration                  | Change configurations   | Изменение конфигураций                           | 