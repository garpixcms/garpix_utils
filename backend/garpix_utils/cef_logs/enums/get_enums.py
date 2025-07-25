from django.conf import settings
from django.utils.module_loading import import_string

DeviceEventClass = import_string(
    getattr(settings, 'CEF_LOG_DEVICE_EVENT_CLASS', 'garpix_utils.cef_logs.enums.enums.DeviceEventClass'))
CEFSeverityLevel = import_string(
    getattr(settings, 'CEF_LOG_SEVERITY_LEVEL', 'garpix_utils.cef_logs.enums.enums.CEFSeverityLevel'))
CEFOutcome = import_string(
    getattr(settings, 'CEF_LOG_OUTCOME', 'garpix_utils.cef_logs.enums.enums.CEFOutcome'))
