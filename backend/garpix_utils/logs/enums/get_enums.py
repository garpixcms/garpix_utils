from django.conf import settings
from django.utils.module_loading import import_string

ActionType = import_string(
    getattr(settings, 'GARPIX_LOG_ACTION_TYPE', 'garpix_utils.logs.enums.action_type.ActionTypeDefault'))
ActionResult = import_string(
    getattr(settings, 'GARPIX_LOG_ACTION_RESULT', 'garpix_utils.logs.enums.action_result.ActionResultDefault'))
ActionLevel = import_string(
    getattr(settings, 'GARPIX_LOG_ACTION_LEVEL', 'garpix_utils.logs.enums.action_level.ActionLevelDefault'))
Action = import_string(getattr(settings, 'GARPIX_LOG_ACTION', 'garpix_utils.logs.enums.action.ActionDefault'))
