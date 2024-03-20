import random
import string
from uuid import uuid4


def get_random_string(size=8, chars=string.ascii_uppercase + string.digits):
    """
    Получает случайную строку указанного размера и с указанными символами.
    """
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))

def get_uuid4_hash():
    """
    Возвращает строку с UUID
    """
    return str(uuid4()).replace('-', '')


class GenerateHash:

    def __init__(self, hash_length=32):
        self.hash_length = hash_length

    def __call__(self):
        return get_random_string(self.hash_length, chars=string.ascii_letters + string.digits)

    def deconstruct(self):
        return ('garpix_utils.string.GenerateHash', [self.hash_length], {})
