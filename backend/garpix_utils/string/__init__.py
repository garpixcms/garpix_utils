import random
import string


def get_random_string(size=8, chars=string.ascii_uppercase + string.digits):
    """
    Получает случайную строку указанного размера и с указанными символами.
    """
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))
