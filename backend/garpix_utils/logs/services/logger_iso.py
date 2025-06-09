import socket
from datetime import datetime, timezone

from django.conf import settings
import logging

from garpix_utils.logs.enums.get_enums import ActionResult
from garpix_utils.logs.services.action_element import ActionElement


class LoggerIso:

    def __init__(self, logger_name=getattr(settings, "ISO_LOGS_NAME", __name__)):
        self.logger = logging.getLogger(logger_name)

    def create_log(self, action: ActionElement, obj, obj_address, result: ActionResult,
                   params=None, sbj=None, sbj_address=None, msg=''):

        dt = datetime.now(timezone.utc).astimezone()

        log = f'time = {dt.isoformat(timespec="seconds")} | id={action.id} | act=\"{action.name}\"'
        log += f' | sbj=\"{sbj}\"' if sbj else ''
        log += f' | sbj_addr=\"{sbj_address}\"' \
               f' | act_type=\"{action.type.value}\"' \
               f' | lvl=\"{action.level.value}\" | obj=\"{obj}\"' \
               f' | obj_addr=\"{obj_address}\"' \
               f' | result=\"{result.value}\"'
        log += f' | change=\"{params}\"' if params else ''
        log += f' | msg=\"{msg}\"'
        hostname, local_ip = self.get_host_info()
        log += f' | host=\"{hostname}\"' \
               f' | host_addr=\"{local_ip}\"'\
               f' | vendor=\"{getattr(settings, "ISO_LOGS_VENDOR", "Garpix")}\"'\
               f' | product=\"{getattr(settings, "ISO_LOGS_PRODUCT", "Default product name")}\"'
        return log

    def write(self, action: ActionElement, obj, obj_address, result: ActionResult, params=None, sbj=None, sbj_address=None, msg=""):
        log = self.create_log(action, obj, obj_address, result, params, sbj, sbj_address, msg)
        self.logger.info(log)

    def write_string(self, string):
        self.logger.info(string)

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
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return hostname, local_ip
