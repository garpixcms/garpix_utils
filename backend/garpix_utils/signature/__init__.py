import hashlib
from collections import OrderedDict


def make_str(variable):
    """
    Превращает рекурсивно словарь (или другую переменную) в строку
    :param variable:
    :return:
    """
    s = ''
    if type(variable) in (dict, OrderedDict):
        for k, v in variable.items():
            s += '{k}{v}'.format(
                k=k,
                v=make_str(v),
            )
    elif type(variable) in (list, tuple):
        for v in variable:
            s += make_str(v)
    else:
        s += str(variable)
    return s


def recursive_sort(params):
    """
    Рекурсивно сортирует словарь или список.
    :param params:
    :return:
    """
    if type(params) == dict:
        sorted_params = OrderedDict(sorted(params.items(), key=lambda t: t[0]))
        for k, v in sorted_params.items():
            sorted_params[k] = recursive_sort(v)
        return sorted_params
    elif type(params) in (list, tuple):
        params = list(params)
        for index, v in enumerate(params):
            params[index] = recursive_sort(v)
        return sorted(params)
    return params


def make_signature_sha512(params, signature_key='sig', secret='secret'):
    """
    Создает сигнатуру по указанным параметрам с хэшированием SHA-512.
    Алгоритм:
    1. Берет словарь параметров, удаляет оттуда параметр с ключом сигнатуры (см. переменную signature_key, по умолчанию значение "sig")
    2. Получившийся словарь сортирует по названию ключа в алфавитном порядке. Все вложенные данные тоже сортируются по ключу, списочные - просто по алфавиту.
    3. Последовательно конкатенирует ключ со значением в единую строку.
    4. В конце конкатенирует значение переменной secret (по умолчанию равна "secret").
    5. Хэширует по алгоритму SHA-512 и возвращает строку в нижнем регистре.
    6. Возвращает получившийся результат.
    ПРИМЕР:
    1. Было: {'a': 'xxx', 'c': 'ggg', 'b': '111', 'sig': '123', 'd': [3, 1, 2], 'e': {'b': '2', 'a': '1'}}
    Стало: {'a': 'xxx', 'c': 'ggg', 'b': '111', 'd': [3, 1, 2], 'e': {'b': '2', 'a': '1'}}
    2. Было: {'a': 'xxx', 'c': 'ggg', 'b': '111', 'd': [3, 1, 2], 'e': {'b': '2', 'a': '1'}}
    Стало: {'a': 'xxx', 'b': '111', 'c': 'ggg', 'd': [1, 2, 3], 'e': {'a': '1', 'b': '2'}}
    3. Было: {'a': 'xxx', 'b': '111', 'c': 'ggg', 'd': [1, 2, 3], 'e': {'a': '1', 'b': '2'}}
    Стало: 'axxxb111cgggd123ea1b2'
    4. Было: 'axxxb111cgggd123ea1b2'
    Стало: 'axxxb111cgggd123ea1b2secret'
    5. Было: 'axxxb111cgggd123ea1b2secret'
    Стало: '2123086085ec1fe67595d7b3d2b6a0dbf3f33e528d78366b8d62d7f0a7e3c090077b0f7b8dc84921a6087aa57b8284bd1e74702df7a16e96f73f627e6eea815a'
    :param params: dict - словарь параметров. Если присутствует signature_key, то он будет удален.
    :param signature_key: str - ключ параметра с сигнатурой. По умолчанию "sig".
    :param secret: str - секретный ключ, который будет приконкатенирован в конце перед хэшированием.
    :return:
    """
    if signature_key in params:
        del params[signature_key]
    s = make_str(recursive_sort(params)) + secret
    return str(hashlib.sha512(s.encode('utf-8')).hexdigest()).lower()
