from enum import Enum


class ActionTypeDefault(Enum):
    authentication = "Идентификация и аутентификация субъекта доступа"
    user_account = "Управление учетными записями пользователей"
    user_access_attribute = "Управление атрибутами доступа"
    access_information = "Доступ к защищаемой информации"
    delete_information = "Удаление информации"
    create_information = "Добавление информации"
    change_information = "Изменение информации"
    change_configuration = "Изменение конфигураций"
