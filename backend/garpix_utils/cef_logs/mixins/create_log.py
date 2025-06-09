from django.contrib.auth import get_user_model


from garpix_utils.cef_logs.event import (
    DataDeleteEvent,
    DataCreateEvent,
    DataModifyEvent,
    UserDeleteEvent,
    UserCreateEvent,
    UserUpdateEvent,
)
from garpix_utils.cef_logs.utils import get_changed_fields, get_changed_m2m_fields

User = get_user_model()


class CreateLogMixin:
    log_msg_delete = None
    log_msg_create = None
    log_msg_change = None

    @staticmethod
    def log_delete(request, obj):
        title = str(obj)

        msg = (
            CreateLogMixin.log_msg_delete
            if CreateLogMixin.log_msg_delete
            else f"Объект {title}(id={obj.pk}) модели {obj.__class__.__name__} был удален"
        )
        if obj.__class__ == User:
            return (UserDeleteEvent(), {"request": request, "user": request.user, "msg": msg})
        else:
            return (DataDeleteEvent(), {"request": request, "user": request.user, "msg": msg})

    @staticmethod
    def logs_change_or_create(request, obj, change):
        title = str(obj)

        if change:
            changed_fields = get_changed_fields(obj)
            events = []
            for field, difference in changed_fields.items():
                if CreateLogMixin.log_msg_change:
                    msg = CreateLogMixin.log_msg_change
                else:
                    msg = f"Изменен параметр {field} с {difference['old']} на {difference['new']} в модели {obj.__class__.__name__} у объекта {title}(id={obj.pk})"
                if obj.__class__ == User:
                    events.append(
                        (UserUpdateEvent(), {"request": request, "user": request.user, "msg": msg})
                    )
                else:
                    events.append(
                        (DataModifyEvent(), {"request": request, "user": request.user, "msg": msg})
                    )
        else:
            if CreateLogMixin.log_msg_create:
                msg = CreateLogMixin.log_msg_create
            else:
                msg = f"Создан объект {title} модели {obj.__class__.__name__}"

            if obj.__class__ == User:
                events = [(UserCreateEvent(), {"request": request, "user": request.user, "msg": msg})]
            else:
                events = [(DataCreateEvent(), {"request": request, "user": request.user, "msg": msg})]
        return events

    @staticmethod
    def logs_change_m2m_field(
        request, admin_obj_super, form, formsets, change, exclude_fields=[]
    ):
        _obj = form.instance
        obj = _obj.__class__.objects.get(pk=_obj.pk) if change else None

        old_obj_fields = {}

        for field in obj._meta.get_fields():
            field_name = field.name
            if field.many_to_many and hasattr(obj, field_name):
                old_object_manager = getattr(obj, field_name)
                old_obj_fields.update(
                    {
                        field_name: set(
                            [str(_obj) for _obj in list(old_object_manager.all())]
                        )
                    }
                )

        admin_obj_super.save_related(request, form, formsets, change)
        params = get_changed_m2m_fields(obj, old_obj_fields, exclude_fields)

        if not params:
            return []

        events = []

        for key, difference in params.items():
            if CreateLogMixin.log_msg_change:
                msg = CreateLogMixin.log_msg_change
            else:
                msg = f"Изменен параметр {key} в модели {obj.__class__.__name__} у объекта {str(obj)}(id={obj.pk}). "
                if difference["added"]:
                    msg += f"Добавлены {difference['added']}"
                if difference["removed"]:
                    msg += f"Удалены {difference['removed']}"

            events.append(
                (DataModifyEvent(), {"request": request, "user": request.user, "msg": msg})
            )

        return events
