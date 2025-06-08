from garpix_utils.logs.enums.get_enums import ActionType, ActionLevel


class ActionElement:

    def __init__(self, action_id: int, action_type: ActionType, name: str, level: ActionLevel):
        self.id = action_id
        self.name = name
        self.type = action_type
        self.level = level
