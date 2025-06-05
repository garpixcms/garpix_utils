from garpix_utils.logs.loggers import ib_logger
from garpix_utils.logs.services.logger_iso import LoggerIso, ActionResult
from garpix_utils.logs.enums.get_enums import Action
from garpix_utils.logs.utils import get_changed_fields



class LogAdminSolo:

    @staticmethod
    def logs_change_or_create(request, obj, change):
        if not change:
            return

        changed_fields = get_changed_fields(obj)
        action = Action.configuration_change.value

        logs = []
        for field, difference in changed_fields.items():
            msg = f'Изменен параметр {field} с {difference["old"]} на {difference["new"]} в {obj.__class__._meta.verbose_name})'
            logs.append(ib_logger.create_log(action=action,
                                    result=ActionResult.success,
                                    sbj=request.user.username,
                                    sbj_address=LoggerIso.get_client_ip(request),
                                    msg=msg))
        return logs


    def save_model(self, request, obj, form, change):
        logs = self.logs_change_or_create(request, obj, change)
        super().save_model(request, obj, form, change)
        for log in logs:
            ib_logger.write_string(log)
