import string
from unittest.mock import patch

from rest_framework.test import APITestCase

from garpix_utils.string import get_random_string, get_uuid4_hash, GenerateHash


class GetRandomStringTest(APITestCase):
    def setUp(self) -> None:
        self.params = [
            [
                (8, string.ascii_uppercase),
                (string.digits, string.ascii_lowercase),
            ],
            [
                (16, string.ascii_lowercase),
                (string.digits, string.ascii_uppercase),
            ],
            [
                (32, string.digits),
                (string.ascii_lowercase, string.ascii_uppercase)
            ]
        ]

    def test_get_random_string(self) -> None:
        for param in self.params:
            rand = get_random_string(*param[0])
            self.assertEqual(len(rand), param[0][0])
            self.assertFalse(set(param[1][0] + param[1][1]).intersection(set(rand)))

    def test_generate_hash(self) -> None:
        for param in self.params:
            hash_generator = GenerateHash(param[0][0])
            hash_ = hash_generator()
            self.assertEqual(len(hash_), param[0][0])


class GetUuid4HashTest(APITestCase):
    @patch("garpix_utils.string.uuid4")
    def test_get_uuid4_hash(self, uuid4) -> None:
        uuid4.return_value = "UU-ID-4"
        self.assertEqual(get_uuid4_hash(), "UUID4")
