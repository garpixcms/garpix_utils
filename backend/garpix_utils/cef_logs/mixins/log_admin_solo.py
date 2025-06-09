from garpix_utils.cef_logs.event import DataModifyEvent
from garpix_utils.cef_logs.utils import get_changed_fields


class LogAdminSolo:
    @staticmethod
    def logs_change_or_create(request, obj, change):
        if not change:
            return []

        changed_fields = get_changed_fields(obj)

        events = []
        for field, difference in changed_fields.items():
            msg = f"Изменен параметр {field} с {difference['old']} на {difference['new']} в {obj.__class__._meta.verbose_name})"
            events.append((DataModifyEvent(), {"request": request, "user": request.user, "msg": msg}))
        return events

    def save_model(self, request, obj, form, change):
        events = self.logs_change_or_create(request, obj, change)
        super().save_model(request, obj, form, change)
        if events:
            for event, args in events:
                event(**args)
