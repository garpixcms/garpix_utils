from django.conf import settings
from garpix_utils.logs.services.logger_iso import LoggerIso

ib_logger = LoggerIso(settings.IB_ISO_LOGS_NAME)
system_logger = LoggerIso(settings.SYSTEM_ISO_LOGS_NAME)
