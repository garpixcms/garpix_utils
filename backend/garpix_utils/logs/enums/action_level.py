from enum import Enum


class ActionLevelDefault(Enum):
    info = 'Информация'
    warning = 'Предупреждение'
    error = 'Ошибка'
    critical = 'Критическая ошибка'
