import re
import socket

from django.conf import settings


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR", None)
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR", None)
    return ip


def get_host_ip():
    """Получает IP адрес хоста"""
    try:
        host = socket.gethostname()
        return socket.gethostbyname(host)
    except:
        return "127.0.0.1"


def get_hostname():
    """Получает валидное имя хоста для CEF логирования"""
    domain = getattr(settings, "SITE_URL", None)
    if domain:
        hostname = domain.split("://")[-1].split("/")[0]  # Убираем протокол и путь
    else:
        try:
            hostname = socket.gethostname()
        except:
            hostname = None

    # CEF regex pattern для dhost поля
    pattern = r"^[A-Za-z0-9][A-Za-z0-9\.\-]*$"

    if hostname and re.match(pattern, hostname):
        return hostname
    else:
        # Возвращаем IP если hostname не соответствует pattern
        return get_host_ip()
