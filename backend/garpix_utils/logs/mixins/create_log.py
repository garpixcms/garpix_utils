from garpix_utils.logs.enums.get_enums import Action
from garpix_utils.logs.services.logger_iso import LoggerIso, ActionResult
from garpix_utils.logs.utils import get_changed_fields, get_changed_m2m_fields


class CreateLogMixin:
    log_msg_delete = None
    log_msg_create = None
    log_msg_change = None
    

    @staticmethod
    def log_delete(logger, request, obj, action):

        title = str(obj)

        msg = CreateLogMixin.log_msg_delete if CreateLogMixin.log_msg_delete else f'Объект {title}(id={obj.pk}) модели {obj.__class__.__name__} был удален'
        return logger.create_log(action=action,
                                 result=ActionResult.success,
                                 sbj=request.user.username,
                                 sbj_address=LoggerIso.get_client_ip(request),
                                 msg=msg)

    @staticmethod
    def logs_change_or_create(logger, request, obj, change, action_change=None, action_create=None):

        title = str(obj)

        if change:
            changed_fields = get_changed_fields(obj)
            action = action_change or Action.any_entity_change.value
            change_logs = []
            for field, difference in changed_fields.items():
                if CreateLogMixin.log_msg_change:
                    msg = CreateLogMixin.log_msg_change
                else:
                    msg = f'Изменен параметр {field} с {difference["old"]} на {difference["new"]} в модели {obj.__class__.__name__} у объекта {title}(id={obj.pk})'
                change_logs.append(logger.create_log(action=action,
                                                    result=ActionResult.success,
                                                    sbj=request.user.username,
                                                    sbj_address=LoggerIso.get_client_ip(request),
                                                    msg=msg))
        else:
            action = action_create or Action.any_entity_create.value
            if CreateLogMixin.log_msg_create:
                msg = CreateLogMixin.log_msg_create
            else:
                msg = f'Создан объект {title} модели {obj.__class__.__name__}'

            change_logs = [
                logger.create_log(
                    action=action,
                    result=ActionResult.success,
                    sbj=request.user.username,
                    sbj_address=LoggerIso.get_client_ip(request),
                    msg=msg
                )
            ]    
            return change_logs
        

    @staticmethod
    def logs_change_m2m_field(logger, request, admin_obj_super, form, formsets, change, action_change=None, exclude_fields=[]):

        _obj = form.instance
        obj = _obj.__class__.objects.get(pk=_obj.pk) if change else None

        old_obj_fields = {}

        changed_fields = ''
        for field in obj._meta.get_fields():
            field_name = field.name
            if field.many_to_many and hasattr(obj, field_name):
                old_object_manager = getattr(obj, field_name)
                old_obj_fields.update({
                    field_name: set([str(_obj) for _obj in list(old_object_manager.all())])
                })

        admin_obj_super.save_related(request, form, formsets, change)
        params = get_changed_m2m_fields(obj, old_obj_fields, exclude_fields)
        action = action_change or Action.any_entity_change.value

        if not params:
            return
        
        logs = []

        for key, difference in params.items():
            if CreateLogMixin.log_msg_change:
                msg = CreateLogMixin.log_msg_change
            else:
                msg = f'Изменен параметр {key} в модели {obj.__class__.__name__} у объекта{str(obj)}(id={obj.pk}). '
                if difference['added']:
                    msg += f'Добавлены {difference["added"]}'
                if difference['removed']:
                    msg += f'Удалены {difference["removed"]}'

                logs.append(logger.create_log(action=action,
                            result=ActionResult.success,
                            sbj=request.user.username,
                            sbj_address=LoggerIso.get_client_ip(request),
                            msg=msg))

        return logs
