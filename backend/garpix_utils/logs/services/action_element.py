from garpix_utils.logs.enums.get_enums import ActionType, ActionLevel


def get_level(code: int) -> ActionLevel:
    if code <= 3:
        return ActionLevel.low
    elif code <= 6:
        return ActionLevel.medium
    elif code <= 9:
        return ActionLevel.high
    elif code <= 10:
        return ActionLevel.very_high
    else:
        raise ValueError(f"Invalid code: {code}. Value must be between 1 and 10.")


class ActionElement:

    def __init__(self, action_id: int, action_type: ActionType, name: str, code: int):
        """
        Args:
            action_id: Идентификатор действия.
            action_type: Тип действия.
            name: Название действия.
            code: Код действия (от 1 до 10)
        """
        self.level = get_level(code)
        self.id = action_id
        self.code = code
        self.name = name
        self.type = action_type
