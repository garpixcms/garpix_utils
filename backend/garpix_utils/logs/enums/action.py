from enum import Enum

from garpix_utils.logs.enums.get_enums import ActionType, ActionLevel
from garpix_utils.logs.services.action_element import ActionElement


class ActionDefault(Enum):
    # 100-199 | Управление учетными записями пользователей
    user_registration = ActionElement(100, action_type=ActionType.user_account, name='Registration', code=7)
    user_create = ActionElement(101, action_type=ActionType.user_account, name='Create user', code=7)
    user_change = ActionElement(102, action_type=ActionType.user_account, name='Change user parameters', code=6)
    user_delete = ActionElement(103, action_type=ActionType.user_account, name='Delete user', code=8)

    # 200-299 | Идентификация и аутентификация субъекта доступа
    user_login = ActionElement(200, action_type=ActionType.authentication, name='System Login', code=6)
    user_logout = ActionElement(201, action_type=ActionType.authentication, name='System Logout', code=4)
    user_fail_login = ActionElement(202, action_type=ActionType.authentication, name='System Login', code=8)

    # 300-399 | Управление атрибутами доступа
    user_access = ActionElement(300, action_type=ActionType.user_access_attribute, name='Change user privileges', code=7)
    group_create = ActionElement(301, action_type=ActionType.user_access_attribute, name='Create user group', code=6)
    group_change = ActionElement(302, action_type=ActionType.user_access_attribute, name='Change user group', code=6)
    group_delete = ActionElement(303, action_type=ActionType.user_access_attribute, name='Delete user group', code=8)
    group_add_user = ActionElement(304, action_type=ActionType.user_access_attribute, name='Add user account to user group', code=6)
    group_delete_user = ActionElement(305, action_type=ActionType.user_access_attribute, name='Delete user account from user group', code=6)

    # 400-499 | Доступ к защищаемой информации
    user_exist = ActionElement(400, action_type=ActionType.access, name='Check user existence', code=3)
    file_download = ActionElement(401, action_type=ActionType.download, name='Download file', code=6)

    # 500-599 | Удаление информации
    any_entity_delete = ActionElement(500, action_type=ActionType.delete, name='Delete entities', code=8)

    # 600-699 | Добавление информации
    any_entity_create = ActionElement(600, action_type=ActionType.create, name='Create entities', code=6)
    file_upload = ActionElement(601, action_type=ActionType.upload, name='Upload file', code=6)

    # 700-799 | Изменение информации
    any_entity_change = ActionElement(700, action_type=ActionType.change, name='Change entities', code=6)

    # 800-899 | Изменение конфигураций
    configuration_change = ActionElement(800, action_type=ActionType.configuration, name='Change configurations', code=8)

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
