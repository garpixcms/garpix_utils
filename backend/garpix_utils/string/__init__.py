import random
import string
from uuid import uuid4


def get_random_string(size=8, chars=string.ascii_uppercase + string.digits):
    """
    Получает случайную строку указанного размера и с указанными символами.
    """
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))

def get_uuid4_hash(size=32):
    uuid = uuid4()
    return str(uuid).replace('-', '')[:size]


class GenerateHash:

    def __init__(self, hash_length=32):
        self.hash_length = hash_length

    def __call__(self):
        if self.hash_length > 32:
            return get_random_string(self.hash_length, chars=string.ascii_letters + string.digits)
        return get_uuid4_hash(self.hash_length)

    def deconstruct(self):
        return ('garpix_utils.string.GenerateHash', [self.hash_length], {})
