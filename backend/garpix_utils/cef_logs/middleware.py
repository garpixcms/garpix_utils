import logging
import os
import time

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from garpix_utils.cef_logs.enums.get_enums import CEFOutcome
from garpix_utils.cef_logs.event import HttpErrorEvent, HttpEvent


class CEFHttpLoggingMiddleware(MiddlewareMixin):
    """
    Middleware для логирования HTTP запросов в формате CEF.

    Логирует:
    - Все HTTP запросы (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS, CONNECT, TRACE)
      с уровнем Low через универсальное HttpEvent
    - HTTP ошибки (статус >= 400) с уровнем Medium через HttpErrorEvent
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)
        # Пути, которые нужно исключить из логирования
        self.excluded_paths = getattr(
            settings,
            "CEF_LOGGING_EXCLUDED_PATHS",
            ["/admin/jsi18n/", "favicon.ico"],
        )
        super().__init__(get_response)

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        end_time = time.time()
        response_time = int((end_time - start_time) * 1000)  # в миллисекундах

        if not self._is_excluded_path(request.path):
            self._log_request(request, response, response_time, start_time, end_time)

        return response

    def _is_excluded_path(self, path):
        for excluded_path in self.excluded_paths:
            if path.startswith(excluded_path):
                return True
        return False

    def _is_file_request(self, path):
        """
        Проверяет, является ли запрос запросом к статическому или медиа файлу.
        """
        static_url = getattr(settings, "STATIC_URL", "/static/")
        media_url = getattr(settings, "MEDIA_URL", "/media/")

        return path.startswith(static_url) or path.startswith(media_url)

    def _log_request(self, request, response, response_time, start_time, end_time):
        method = request.method.upper()

        # Определяем outcome на основе статуса ответа
        if 200 <= response.status_code < 300:
            outcome = CEFOutcome.SUCCESS.value
        elif 300 <= response.status_code < 400:
            outcome = CEFOutcome.PARTIAL.value
        elif 400 <= response.status_code < 500:
            outcome = CEFOutcome.DENIED.value
        elif response.status_code >= 500:
            outcome = CEFOutcome.FAILURE.value
        else:
            outcome = CEFOutcome.UNKNOWN.value

        # Базовые данные для CEF события
        event_data = {
            "request": request,
            "user": getattr(request, "user", None)
            if hasattr(request, "user")
            else None,
            "msg": f"{method} {request.path}",
            "outcome": outcome,
            "HTTPStatus": str(response.status_code),
            "ResponseTime": str(response_time) + "ms",
            "UserAgent": request.META.get("HTTP_USER_AGENT", "Unknown"),
            "start": int(start_time),
            "end": int(end_time),
        }

        # Добавляем информацию о теле запроса для POST/PUT/PATCH
        if method in ["POST", "PUT", "PATCH"] and hasattr(request, "body"):
            try:
                body_size = len(request.body)
                event_data["RequestBodySize"] = str(body_size)
            except Exception:
                pass

        # Добавляем параметры для GET запросов
        if method == "GET" and request.GET:
            params_count = len(request.GET)
            event_data["QueryParamsCount"] = str(params_count)

        # Логирование доступа к файлам
        if method == "GET" and self._is_file_request(request.path):
            filename = os.path.basename(request.path)
            if filename:
                event_data["fname"] = filename

        try:
            # Выбираем соответствующий тип события
            if response.status_code >= 400:
                event = HttpErrorEvent()
                event_data["msg"] = f"{request.path} - HTTP {response.status_code}"
            else:
                event = HttpEvent()

            event(**event_data)

        except Exception as e:
            self.logger.error(f"Error logging request: {e}")

    def process_exception(self, request, exception):
        try:
            event_data = {
                "request": request,
                "user": getattr(request, "user", None)
                if hasattr(request, "user")
                else None,
                "msg": f"{request.method} {request.path} - Exception: {str(exception)}",
                "outcome": CEFOutcome.FAILURE.value,
                "HTTPStatus": "500",
                "UserAgent": request.META.get("HTTP_USER_AGENT", "Unknown"),
                "ExceptionType": str(type(exception).__name__),
            }

            event = HttpErrorEvent()
            event(**event_data)

        except Exception as e:
            self.logger.error(f"Error logging exception: {e}")
        return None
