from enum import Enum


class ActionTypeDefault(Enum):
    authentication = "authentication"
    user_account = "user_account"
    user_access_attribute = "user_access_attribute"
    access = "access"
    delete = "delete"
    create = "create"
    change = "change"
    configuration = "configuration"
    upload = "upload"
    download = "download"
