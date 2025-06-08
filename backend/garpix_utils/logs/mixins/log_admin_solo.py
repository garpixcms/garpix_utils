from garpix_utils.logs.loggers import ib_logger
from garpix_utils.logs.services.logger_iso import LoggerIso, ActionResult
from garpix_utils.logs.enums.get_enums import Action


class LogAdminSolo:

    @staticmethod
    def log_change_or_create(request, obj, change):
        old_obj = obj.__class__.objects.get(pk=obj.pk) if change else None
        changed_fields = ''
        fields = obj._meta.fields
        for field in fields:
            field_name = field.name
            old_value = getattr(old_obj, field_name)
            new_value = getattr(obj, field_name)
            if old_obj and old_value != new_value:
                changed_fields += f'{field.verbose_name}: {old_value} -> {new_value};'
        params = changed_fields
        action = Action.configuration_change.value
        msg = f'{obj.__class__._meta.verbose_name} был изменен'

        return ib_logger.create_log(action=action,
                                    obj=obj.__class__.__name__,
                                    obj_address=request.path,
                                    result=ActionResult.success,
                                    sbj=request.user.username,
                                    params=params,
                                    sbj_address=LoggerIso.get_client_ip(request),
                                    msg=msg)

    def save_model(self, request, obj, form, change):
        log = self.log_change_or_create(request, obj, change)
        super().save_model(request, obj, form, change)
        ib_logger.write_string(log)
