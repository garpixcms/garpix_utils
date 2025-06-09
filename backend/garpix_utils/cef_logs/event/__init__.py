from .base import BaseEvent

from .enevts import (
    # Аутентификация
    LoginEvent,
    LoginFailedEvent,
    LoginCriticalEvent,
    LogoutEvent,
    PasswordChangeEvent,
    PasswordResetEvent,
    # Авторизация и доступ
    AccessGrantedEvent,
    AccessDeniedEvent,
    PermissionChangeEvent,
    RoleChangeEvent,
    # HTTP запросы
    HttpEvent,  # Универсальный класс для всех HTTP запросов
    HttpErrorEvent,
    # API события
    ApiCallEvent,
    ApiErrorEvent,
    ApiRateLimitEvent,
    # Безопасность
    SecurityViolationEvent,
    MalwareDetectedEvent,
    IntrusionAttemptEvent,
    SuspiciousActivityEvent,
    # Системные события
    SystemStartEvent,
    SystemStopEvent,
    SystemErrorEvent,
    DatabaseErrorEvent,
    # Пользовательские действия
    UserCreateEvent,
    UserUpdateEvent,
    UserDeleteEvent,
    UserActivityEvent,
    # Данные
    DataAccessEvent,
    DataModifyEvent,
    DataDeleteEvent,
    DataExportEvent,
    DataCreateEvent,
    # Файловые операции
    FileUploadEvent,
    FileDownloadEvent,
    FileDeleteEvent,
    FileAccessEvent,
)

__all__ = [
    "BaseEvent",
    # Аутентификация
    "LoginEvent",
    "LoginFailedEvent",
    "LoginCriticalEvent",
    "LogoutEvent",
    "PasswordChangeEvent",
    "PasswordResetEvent",
    # Авторизация и доступ
    "AccessGrantedEvent",
    "AccessDeniedEvent",
    "PermissionChangeEvent",
    "RoleChangeEvent",
    # HTTP запросы
    "HttpEvent",  # Универсальный класс для всех HTTP запросов
    "HttpErrorEvent",
    # API события
    "ApiCallEvent",
    "ApiErrorEvent",
    "ApiRateLimitEvent",
    # Безопасность
    "SecurityViolationEvent",
    "MalwareDetectedEvent",
    "IntrusionAttemptEvent",
    "SuspiciousActivityEvent",
    # Системные события
    "SystemStartEvent",
    "SystemStopEvent",
    "SystemErrorEvent",
    "DatabaseErrorEvent",
    # Пользовательские действия
    "UserCreateEvent",
    "UserUpdateEvent",
    "UserDeleteEvent",
    "UserActivityEvent",
    # Данные
    "DataAccessEvent",
    "DataModifyEvent",
    "DataDeleteEvent",
    "DataExportEvent",
    "DataCreateEvent",
    # Файловые операции
    "FileUploadEvent",
    "FileDownloadEvent",
    "FileDeleteEvent",
    "FileAccessEvent",
]
