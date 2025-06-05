from enum import Enum

from garpix_utils.logs.enums.get_enums import ActionType, ActionLevel
from garpix_utils.logs.services.action_element import ActionElement


class ActionDefault(Enum):
    # 100-199 | Управление учетными записями пользователей
    user_registration = ActionElement(id=100, action_type=ActionType.user_account, name='Registration', code=7)
    user_create = ActionElement(id=101, action_type=ActionType.user_account, name='Create user', code=7)
    user_change = ActionElement(id=102, action_type=ActionType.user_account, name='Change user parameters', code=6)
    user_delete = ActionElement(id=103, action_type=ActionType.user_account, name='Delete user', code=8)

    # 200-299 | Идентификация и аутентификация субъекта доступа
    user_login = ActionElement(id=200, action_type=ActionType.authentication, name='System Login', code=6)
    user_logout = ActionElement(id=201, action_type=ActionType.authentication, name='System Logout', code=4)
    user_fail_login = ActionElement(id=202, action_type=ActionType.authentication, name='System Login', code=8)

    # 300-399 | Управление атрибутами доступа
    user_access = ActionElement(id=300, action_type=ActionType.user_access_attribute, name='Change user privileges', code=7)
    group_create = ActionElement(id=301, action_type=ActionType.user_access_attribute, name='Create user group', code=6)
    group_change = ActionElement(id=302, action_type=ActionType.user_access_attribute, name='Change user group', code=6)
    group_delete = ActionElement(id=303, action_type=ActionType.user_access_attribute, name='Delete user group', code=8)
    group_add_user = ActionElement(id=304, action_type=ActionType.user_access_attribute, name='Add user account to user group', code=6)
    group_delete_user = ActionElement(id=305, action_type=ActionType.user_access_attribute, name='Delete user account from user group', code=6)

    # 400-499 | Доступ к защищаемой информации
    user_exist = ActionElement(id=400, action_type=ActionType.access_information, name='Check user existence', code=3)

    # 500-599 | Удаление информации
    any_entity_delete = ActionElement(id=500, action_type=ActionType.delete_information, name='Delete entities', code=8)

    # 600-699 | Добавление информации
    any_entity_create = ActionElement(id=600, action_type=ActionType.create_information, name='Create entities', code=6)

    # 700-799 | Изменение информации
    any_entity_change = ActionElement(id=700, action_type=ActionType.change_information, name='Change entities', code=6)

    # 800-899 | Изменение конфигураций
    configuration_change = ActionElement(id=800, action_type=ActionType.change_configuration, name='Change configurations', code=8)

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
