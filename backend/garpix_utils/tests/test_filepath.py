import os
from unittest.mock import patch, MagicMock, call
from datetime import date

from django.conf import settings
from rest_framework.test import APITestCase

from garpix_utils.file.filepath import get_secret_path


class GetSecretPathTest(APITestCase):
    def setUp(self) -> None:
        self.today = date.today()
        self.path = os.path.join(
            f"data/{self.today.year}/{self.today.month}/test/test/test"
        )

    @patch("garpix_utils.file.filepath.get_random_string")
    def test_get_secret_path(self, get_random_string) -> None:
        os.makedirs = MagicMock(return_value=None)
        get_random_string.return_value = "test"
        path = get_secret_path("__test_-file/.txt")
        self.assertEqual(path, os.path.join(self.path, "test-file.txt"))
        get_random_string.assert_has_calls([call(16), call(16), call(16)])
        os.makedirs.assert_called_with(os.path.join(settings.MEDIA_ROOT, self.path))
    
    @patch("garpix_utils.file.filepath.get_random_string")
    def test_get_secret_path_none(self, get_random_string) -> None:
        os.makedirs = MagicMock(return_value=None)
        get_random_string.return_value = "test"
        path = get_secret_path()
        self.assertEqual(path, self.path)
        get_random_string.assert_has_calls([call(16), call(16), call(16)])
        os.makedirs.assert_called_with(os.path.join(settings.MEDIA_ROOT, self.path))
