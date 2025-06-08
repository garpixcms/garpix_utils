from .base import BaseEvent
from ..enums.get_enums import DeviceEventClass, CEFSeverityLevel


# === АУТЕНТИФИКАЦИЯ (1000-1099) ===


class LoginEvent(BaseEvent):
    """Успешный вход в систему - Medium уровень"""

    _event_class = DeviceEventClass.LOGIN
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.MEDIUM.value


class LoginFailedEvent(BaseEvent):
    """Неудачная попытка входа - High уровень"""

    _event_class = DeviceEventClass.LOGIN
    DeviceEventClassID = _event_class.value
    Name = f"{_event_class.label} Failed"
    Severity = CEFSeverityLevel.HIGH.value


class LoginCriticalEvent(BaseEvent):
    """Критический вход (подозрительная активность) - Very High уровень"""

    _event_class = DeviceEventClass.LOGIN
    DeviceEventClassID = _event_class.value
    Name = f"{_event_class.label} Critical"
    Severity = CEFSeverityLevel.VERY_HIGH.value


class LogoutEvent(BaseEvent):
    """Выход из системы - Low уровень"""

    _event_class = DeviceEventClass.LOGOUT
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.LOW.value


class PasswordChangeEvent(BaseEvent):
    """Изменение пароля - Medium уровень"""

    _event_class = DeviceEventClass.PASSWORD_CHANGE
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.MEDIUM.value


class PasswordResetEvent(BaseEvent):
    """Сброс пароля - Medium уровень"""

    _event_class = DeviceEventClass.PASSWORD_RESET
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.MEDIUM.value


# === АВТОРИЗАЦИЯ И ДОСТУП (1100-1199) ===


class AccessGrantedEvent(BaseEvent):
    """Доступ предоставлен - Low уровень"""

    _event_class = DeviceEventClass.ACCESS_GRANTED
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.LOW.value


class AccessDeniedEvent(BaseEvent):
    """Доступ запрещен - Medium уровень"""

    _event_class = DeviceEventClass.ACCESS_DENIED
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.MEDIUM.value


class PermissionChangeEvent(BaseEvent):
    """Изменение разрешений - Medium уровень"""

    _event_class = DeviceEventClass.PERMISSION_CHANGE
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.MEDIUM.value


class RoleChangeEvent(BaseEvent):
    """Изменение роли - Medium уровень"""

    _event_class = DeviceEventClass.ROLE_CHANGE
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.MEDIUM.value


# === HTTP ЗАПРОСЫ (2000-2099) ===


class HttpEvent(BaseEvent):
    """Универсальное HTTP событие - Low уровень"""

    _event_class = DeviceEventClass.HTTP_REQUEST
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.LOW.value


class HttpErrorEvent(BaseEvent):
    """HTTP ошибка - Medium уровень"""

    _event_class = DeviceEventClass.HTTP_ERROR
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.MEDIUM.value


# === API СОБЫТИЯ (2100-2199) ===


class ApiCallEvent(BaseEvent):
    """API вызов - Low уровень"""

    _event_class = DeviceEventClass.API_CALL
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.LOW.value


class ApiErrorEvent(BaseEvent):
    """API ошибка - Medium уровень"""

    _event_class = DeviceEventClass.API_ERROR
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.MEDIUM.value


class ApiRateLimitEvent(BaseEvent):
    """API превышение лимита - Medium уровень"""

    _event_class = DeviceEventClass.API_RATE_LIMIT
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.MEDIUM.value


# === БЕЗОПАСНОСТЬ (3000-3099) ===


class SecurityViolationEvent(BaseEvent):
    """Нарушение безопасности - Very High уровень"""

    _event_class = DeviceEventClass.SECURITY_VIOLATION
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.VERY_HIGH.value


class MalwareDetectedEvent(BaseEvent):
    """Обнаружено вредоносное ПО - Very High уровень"""

    _event_class = DeviceEventClass.MALWARE_DETECTED
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.VERY_HIGH.value


class IntrusionAttemptEvent(BaseEvent):
    """Попытка вторжения - Very High уровень"""

    _event_class = DeviceEventClass.INTRUSION_ATTEMPT
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.VERY_HIGH.value


class SuspiciousActivityEvent(BaseEvent):
    """Подозрительная активность - High уровень"""

    _event_class = DeviceEventClass.SUSPICIOUS_ACTIVITY
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.HIGH.value


# === СИСТЕМНЫЕ СОБЫТИЯ (4000-4099) ===


class SystemStartEvent(BaseEvent):
    """Запуск системы - Medium уровень"""

    _event_class = DeviceEventClass.SYSTEM_START
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.MEDIUM.value


class SystemStopEvent(BaseEvent):
    """Остановка системы - Medium уровень"""

    _event_class = DeviceEventClass.SYSTEM_STOP
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.MEDIUM.value


class SystemErrorEvent(BaseEvent):
    """Системная ошибка - High уровень"""

    _event_class = DeviceEventClass.SYSTEM_ERROR
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.HIGH.value


class DatabaseErrorEvent(BaseEvent):
    """Ошибка базы данных - High уровень"""

    _event_class = DeviceEventClass.DATABASE_ERROR
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.HIGH.value


# === ПОЛЬЗОВАТЕЛЬСКИЕ ДЕЙСТВИЯ (5000-5099) ===


class UserCreateEvent(BaseEvent):
    """Создание пользователя - Low уровень (create)"""

    _event_class = DeviceEventClass.USER_CREATE
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.LOW.value


class UserUpdateEvent(BaseEvent):
    """Обновление пользователя - Low уровень (edit)"""

    _event_class = DeviceEventClass.USER_UPDATE
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.LOW.value


class UserDeleteEvent(BaseEvent):
    """Удаление пользователя - High уровень (delete)"""

    _event_class = DeviceEventClass.USER_DELETE
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.HIGH.value


class UserActivityEvent(BaseEvent):
    """Активность пользователя - Low уровень (view)"""

    _event_class = DeviceEventClass.USER_ACTIVITY
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.LOW.value


# === ДАННЫЕ (6000-6099) ===


class DataAccessEvent(BaseEvent):
    """Доступ к данным - Low уровень (view)"""

    _event_class = DeviceEventClass.DATA_ACCESS
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.LOW.value


class DataModifyEvent(BaseEvent):
    """Изменение данных - Low уровень (edit)"""

    _event_class = DeviceEventClass.DATA_MODIFY
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.LOW.value


class DataDeleteEvent(BaseEvent):
    """Удаление данных - High уровень (delete)"""

    _event_class = DeviceEventClass.DATA_DELETE
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.HIGH.value


class DataExportEvent(BaseEvent):
    """Экспорт данных - Medium уровень"""

    _event_class = DeviceEventClass.DATA_EXPORT
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.MEDIUM.value


class DataCreateEvent(BaseEvent):
    """Создание данных - Low уровень (create)"""

    _event_class = DeviceEventClass.DATA_CREATE
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.LOW.value


# === ФАЙЛОВЫЕ ОПЕРАЦИИ (7000-7099) ===


class FileUploadEvent(BaseEvent):
    """Загрузка файла - Medium уровень (file_upload)"""

    _event_class = DeviceEventClass.FILE_UPLOAD
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.MEDIUM.value


class FileDownloadEvent(BaseEvent):
    """Скачивание файла - Medium уровень (file_download)"""

    _event_class = DeviceEventClass.FILE_DOWNLOAD
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.MEDIUM.value


class FileDeleteEvent(BaseEvent):
    """Удаление файла - High уровень (delete)"""

    _event_class = DeviceEventClass.FILE_DELETE
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.HIGH.value


class FileAccessEvent(BaseEvent):
    """Доступ к файлу - Low уровень (view)"""

    _event_class = DeviceEventClass.FILE_ACCESS
    DeviceEventClassID = _event_class.value
    Name = _event_class.label
    Severity = CEFSeverityLevel.LOW.value
