import abc
from time import time
from typing import Any, Dict, Union

from cef_logger import Event
from cef_logger.schemas import ExtensionFields
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.module_loading import import_string
from pydantic.fields import ModelField

from garpix_utils.cef_logs.enums.get_enums import CEFOutcome
from garpix_utils.cef_logs.utils import get_client_ip, get_host_ip, get_hostname

User = get_user_model()


def truncate_dict_by_model(
        data: Dict[str, Any]
) -> Dict[str, Any]:
    cleaned = data.copy()
    for name, value in list(cleaned.items()):
        field: Union[ModelField, None] = ExtensionFields.__fields__.get(name)
        if not field:
            continue
        max_len = field.field_info.max_length
        if max_len is not None and isinstance(value, str):
            if len(value) > max_len:
                cleaned[name] = value[:max_len]
    return cleaned


class BaseEvent(Event, abc.ABC):
    DeviceVendor = getattr(settings, "CEF_DEVICE_VENDOR", "Garpix")
    DeviceProduct = getattr(settings, "CEF_DEVICE_PRODUCT", "Django Application")
    DeviceVersion = getattr(settings, "CEF_DEVICE_VERSION", "1.0.0")
    EMITTERS = [
        import_string(emmiter)()
        for emmiter in getattr(settings, "CEF_EMITTERS", ("logging.StreamHandler",))
    ]
    Version = 0

    src = None
    dhost = None
    dpt = None
    dst = None
    end = None
    fname = None
    msg = None
    outcome = CEFOutcome.SUCCESS.value
    suid = None
    suser = None

    def __call__(self, **fields):

        fields = truncate_dict_by_model(fields)

        user = fields.pop("user", None)
        request = fields.pop("request", None)
        if "fname" in fields:
            fields["fname"] = fields["fname"].split("/")[-1]
        if user and isinstance(user, User):
            fields["suser"] = user.username
            fields["suid"] = user.id
        if request and not isinstance(request, str):
            if hasattr(request, "build_absolute_uri"):
                fields["request"] = request.build_absolute_uri()
            if hasattr(request, "method"):
                fields["requestMethod"] = request.method
            if hasattr(request, "scheme"):
                fields["app"] = request.scheme
            if hasattr(request, "get_host"):
                fields["dhost"] = request.get_host().split(":")[0]
        if request and hasattr(request, "META"):
            fields["dpt"] = request.META.get("SERVER_PORT", None)
            fields["dst"] = request.META.get("SERVER_ADDR", None)

        if not fields.get("dhost", None):
            fields["dhost"] = get_hostname()
        if not fields.get("dst", None):
            fields["dst"] = get_host_ip()
        if not fields.get("end"):
            fields["end"] = int(time())
        if not fields.get("src"):
            fields["src"] = get_client_ip(request)
        return super().__call__(**fields)
