from django.db import models


class DeviceEventClass(models.IntegerChoices):
    """
    Перечисление типов событий для CEF логов
    Совместимо с Django models.IntegerChoices для использования в полях модели
    """

    # Аутентификация (1000-1099)
    LOGIN = 1001, "System Login"
    LOGOUT = 1002, "System Logout"
    PASSWORD_CHANGE = 1003, "Password Change"
    PASSWORD_RESET = 1004, "Password Reset"

    # Авторизация и доступ (1100-1199)
    ACCESS_GRANTED = 1101, "Access Granted"
    ACCESS_DENIED = 1102, "Access Denied"
    PERMISSION_CHANGE = 1103, "Permission Change"
    ROLE_CHANGE = 1104, "Role Change"

    # HTTP запросы (2000-2099)
    HTTP_REQUEST = 2001, "HTTP Request"  # Универсальное HTTP событие
    HTTP_GET = 2002, "HTTP GET"
    HTTP_POST = 2003, "HTTP POST"
    HTTP_PUT = 2004, "HTTP PUT"
    HTTP_DELETE = 2005, "HTTP DELETE"
    HTTP_PATCH = 2006, "HTTP PATCH"
    HTTP_HEAD = 2007, "HTTP HEAD"
    HTTP_OPTIONS = 2008, "HTTP OPTIONS"
    HTTP_CONNECT = 2009, "HTTP CONNECT"
    HTTP_TRACE = 2010, "HTTP TRACE"
    HTTP_ERROR = 2020, "HTTP Error"

    # API события (2100-2199)
    API_CALL = 2101, "API Call"
    API_ERROR = 2102, "API Error"
    API_RATE_LIMIT = 2103, "API Rate Limit"

    # Безопасность (3000-3099)
    SECURITY_VIOLATION = 3001, "Security Violation"
    MALWARE_DETECTED = 3002, "Malware Detected"
    INTRUSION_ATTEMPT = 3003, "Intrusion Attempt"
    SUSPICIOUS_ACTIVITY = 3004, "Suspicious Activity"

    # Системные события (4000-4099)
    SYSTEM_START = 4001, "System Start"
    SYSTEM_STOP = 4002, "System Stop"
    SYSTEM_ERROR = 4003, "System Error"
    DATABASE_ERROR = 4004, "Database Error"

    # Пользовательские действия (5000-5099)
    USER_CREATE = 5001, "User Create"
    USER_UPDATE = 5002, "User Update"
    USER_DELETE = 5003, "User Delete"
    USER_ACTIVITY = 5004, "User Activity"

    # Данные (6000-6099)
    DATA_ACCESS = 6001, "Data Access"
    DATA_MODIFY = 6002, "Data Modify"
    DATA_DELETE = 6003, "Data Delete"
    DATA_EXPORT = 6004, "Data Export"
    DATA_CREATE = 6005, "Data Create"

    # Файловые операции (7000-7099)
    FILE_UPLOAD = 7001, "File Upload"
    FILE_DOWNLOAD = 7002, "File Download"
    FILE_DELETE = 7003, "File Delete"
    FILE_ACCESS = 7004, "File Access"


class CEFSeverityLevel(models.IntegerChoices):
    """
    Уровни важности для CEF событий (от 1 до 10)
    """

    VERY_LOW = 1, "Very Low"
    LOW = 2, "Low"
    LOW_MEDIUM = 3, "Low Medium"
    MEDIUM_LOW = 4, "Medium Low"
    MEDIUM = 5, "Medium"
    MEDIUM_HIGH = 6, "Medium High"
    HIGH_MEDIUM = 7, "High Medium"
    HIGH = 8, "High"
    VERY_HIGH = 9, "Very High"
    CRITICAL = 10, "Critical"


class CEFOutcome(models.TextChoices):
    """
    Статусы исхода событий для CEF логов
    """

    SUCCESS = "success", "Success"
    FAILURE = "failure", "Failure"
    PARTIAL = "partial", "Partial"
    UNKNOWN = "unknown", "Unknown"
    DENIED = "denied", "Denied"
    BLOCKED = "blocked", "Blocked"
    ALLOWED = "allowed", "Allowed"
