from enum import Enum

from garpix_utils.logs.enums.get_enums import ActionType, ActionLevel
from garpix_utils.logs.services.action_element import ActionElement


class ActionDefault(Enum):
    # 100-199 | Управление учетными записями пользователей
    user_registration = ActionElement(100, ActionType.user_account, 'Регистрация', ActionLevel.info)
    user_create = ActionElement(101, ActionType.user_account, 'Создание пользователя', ActionLevel.info)
    user_change = ActionElement(102, ActionType.user_account, 'Изменение параметров пользователя', ActionLevel.warning)
    user_delete = ActionElement(103, ActionType.user_account, 'Удаление пользователя', ActionLevel.warning)

    # 200-299 | Идентификация и аутентификация субъекта доступа
    user_login = ActionElement(200, ActionType.authentication, 'Вход в систему', ActionLevel.info)
    user_logout = ActionElement(201, ActionType.authentication, 'Выход из системы', ActionLevel.info)

    # 300-399 | Управление атрибутами доступа
    user_access = ActionElement(300, ActionType.user_access_attribute, 'Изменение привилегий пользователя',
                                ActionLevel.warning)
    group_create = ActionElement(301, ActionType.user_access_attribute, 'Создание группы пользователей',
                                 ActionLevel.warning)
    group_change = ActionElement(302, ActionType.user_access_attribute, 'Изменение группы пользователей',
                                 ActionLevel.warning)
    group_delete = ActionElement(303, ActionType.user_access_attribute, 'Удаление группы пользователей',
                                 ActionLevel.warning)
    group_add_user = ActionElement(304, ActionType.user_access_attribute,
                                   'Занесение учетной записи в группу пользователей', ActionLevel.warning)
    group_delete_user = ActionElement(305, ActionType.user_access_attribute,
                                      'Удаление учетной записи из группы пользователей', ActionLevel.warning)

    # 400-499 | Доступ к защищаемой информации
    user_exist = ActionElement(400, ActionType.access_information, 'Проверка существования пользователя',
                               ActionLevel.info)

    # 500-599 | Удаление информации
    any_entity_delete = ActionElement(500, ActionType.delete_information, 'Удаление сущностей', ActionLevel.info)

    # 600-699 | Добавление информации
    any_entity_create = ActionElement(600, ActionType.create_information, 'Создание сущностей', ActionLevel.info)

    # 700-799 | Изменение информации
    any_entity_change = ActionElement(700, ActionType.change_information, 'Изменение сущностей', ActionLevel.info)

    # 800-899 | Изменение конфигураций
    configuration_change = ActionElement(800, ActionType.change_configuration, 'Изменение конфигураций',
                                         ActionLevel.info)

    '''
        100-199 | Управление учетными записями пользователей
        200-299 | Идентификация и аутентификация субъекта доступа
        300-399 | Управление атрибутами доступа
        400-499 | Доступ к защищаемой информации
        500-599 | Удаление информации
        600-699 | Добавление информации
        700-799 | Изменение информации
        800-899 | Изменение конфигураций
    '''
