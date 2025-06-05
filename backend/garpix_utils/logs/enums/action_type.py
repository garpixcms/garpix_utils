from enum import Enum


class ActionTypeDefault(Enum):
    view = "view"
    create = "create"
    edit = "edit"
    logout = "logout"
    login = "login"
    file_upload = "file_upload"
    calc = "calc" # вынести в глс
    file_download = "file_download"
