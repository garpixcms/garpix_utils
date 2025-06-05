import socket
from datetime import datetime, timezone

from django.conf import settings
import logging
import time

from garpix_utils.logs.enums.get_enums import ActionResult
from garpix_utils.logs.services.action_element import ActionElement


class LoggerIso:

    def __init__(self, logger_name=settings.ISO_LOGS_NAME):
        self.logger = logging.getLogger(logger_name)

    def create_log(self, action: ActionElement, result: ActionResult, sbj=None, sbj_address=None, msg='', fname=None):

        dt = datetime.now(timezone.utc).astimezone()
        hostname, local_ip = self.get_host_info()

        log = self.format_cef_log(
            event_class_id=action.type.value,
            name=action.name,
            severity=action.code,
            src=sbj_address,
            dhost=hostname if hostname else local_ip,
            suser=sbj,
            msg=msg,
            fname=fname.split('/')[-1] if fname else '',
            outcome=result.value
        )
        return log

    def write(self, action: ActionElement, result: ActionResult, sbj=None, sbj_address=None, msg="", fname=None):
        log = self.create_log(action, result, sbj, sbj_address, msg, fname)
        self.logger.info(log)

    def write_string(self, string):
        self.logger.info(string)


    @staticmethod
    def format_cef_log(event_class_id, name, severity, **kwargs):
        """
        Форматирует лог в формате CEF вручную.
        Повторяющиеся поля берутся из конфигурации CEF_CONFIG.

        Arguments:
            event_class_id (str): Идентификатор класса события.
            name (str): Название события.
            severity (str): Код события.
            **kwargs: Дополнительные аргументы.

        Return:
            str: Отформатированная строка в формате CEF.
        """

        CEF_CONFIG = {
            'version': '0',
            'device_vendor': getattr(settings, "ISO_LOGS_VENDOR", "Garpix"),
            'device_product': settings.ISO_LOGS_PRODUCT,
            'device_version': getattr(settings, "ISO_LOGS_PRODUCT_VERSION", "1.0.0")
        }

        cef_header = f"CEF:{CEF_CONFIG['version']}|{CEF_CONFIG['device_vendor']}|{CEF_CONFIG['device_product']}|{CEF_CONFIG['device_version']}|{event_class_id}|{name}|{severity}"

        extensions = [f"{key}={value.value}" if hasattr(value, 'value') else f"{key}={value}" for key, value in kwargs.items()]
        extensions.append(f"end={time.time()}")
        cef_log = cef_header + "|" + " ".join(extensions)
        
        return cef_log

    @staticmethod
    def get_client_ip(request):
        # Используется для поулчения адреса субъекта
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    @staticmethod
    def get_host_info() -> (str, str):
        domain = getattr(settings, "SITE_URL", None)
        hostname = domain if domain else socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return hostname, local_ip
