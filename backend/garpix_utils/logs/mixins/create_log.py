from garpix_utils.logs.enums.get_enums import Action
from garpix_utils.logs.services.logger_iso import LoggerIso, ActionResult


class CreateLogMixin:
    log_msg_delete = None
    log_msg_create = None
    log_msg_change = None

    @staticmethod
    def log_delete(logger, request, obj, action):

        title = str(obj)

        msg = CreateLogMixin.log_msg_delete if CreateLogMixin.log_msg_delete else f'Объект {title}(id={obj.pk}) модели {obj.__class__.__name__}  был удален'
        return logger.create_log(action=action,
                                 obj=obj.__class__.__name__,
                                 obj_address=request.path,
                                 result=ActionResult.success,
                                 sbj=request.user.username,
                                 sbj_address=LoggerIso.get_client_ip(request),
                                 msg=msg)

    @staticmethod
    def log_change_or_create(logger, request, obj, change, action_change=None, action_create=None):

        title = str(obj)

        if change:
            old_obj = obj.__class__.objects.get(pk=obj.pk) if change else None
            changed_fields = ''
            fields = obj._meta.fields
            for field in fields:
                field_name = field.name
                if hasattr(obj, field_name):
                    old_value = getattr(old_obj, field_name)
                    new_value = getattr(obj, field_name)
                    if old_obj and old_value != new_value:
                        changed_fields += f'{field.verbose_name}: {old_value} -> {new_value};'

            params = changed_fields
            action = action_change or Action.any_entity_change.value
            msg = CreateLogMixin.log_msg_change if CreateLogMixin.log_msg_change else f'Объект {title}(id={obj.pk}) модели {obj.__class__.__name__} был изменен'
        else:
            action = action_create or Action.any_entity_create.value
            msg = CreateLogMixin.log_msg_create if CreateLogMixin.log_msg_create else f'Объект {title} модели {obj.__class__.__name__} был добавлен'
            params = None

        return logger.create_log(action=action,
                                 obj=obj.__class__.__name__,
                                 obj_address=request.path,
                                 result=ActionResult.success,
                                 sbj=request.user.username,
                                 params=params,
                                 sbj_address=LoggerIso.get_client_ip(request),
                                 msg=msg)
    @staticmethod
    def log_change_m2m_field(logger, request, admin_obj_super, form, formsets, change, action_change=None, exclude_fields=[]):

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
        for field in obj._meta.get_fields():
            field_name = field.name
            if field.many_to_many and hasattr(obj, field_name) and field_name not in exclude_fields:
                new_object_manager = getattr(obj, field_name)
                new_relations = set([str(_obj) for _obj in list(new_object_manager.all())])

                new_old = new_relations - old_obj_fields[field_name]
                old_new = old_obj_fields[field_name] - new_relations

                if new_old or old_new:
                    changed_fields += f'{field.verbose_name}: '
                    if new_old:
                        changed_fields += f'+добавлены {new_old} '
                    if old_new:
                        changed_fields += f'-удалены {old_new} '

        params = changed_fields
        action = action_change or Action.any_entity_change.value

        if params != '':
            msg = CreateLogMixin.log_msg_change if CreateLogMixin.log_msg_change else f'Объект {str(obj)}(id={obj.pk}) модели {obj.__class__.__name__} был изменен'

            return logger.create_log(action=action,
                                     obj=obj.__class__.__name__,
                                     obj_address=request.path,
                                     result=ActionResult.success,
                                     sbj=request.user.username,
                                     params=params,
                                     sbj_address=LoggerIso.get_client_ip(request),
                                     msg=msg)
