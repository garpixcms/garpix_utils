from rest_framework.test import APITestCase
from rest_framework.request import HttpRequest

from garpix_utils.templatetags.url_replace import url_replace


class UrlReplaceTest(APITestCase):
    def test_url_replace(self) -> None:
        request = HttpRequest()
        request.GET["test1"] = "test_value1"
        request.GET["test2"] = "test_value2"
        query_string = url_replace(request, "test1", "test_1")

        self.assertEqual(request.GET["test1"], "test_value1")
        self.assertEqual(request.GET["test2"], "test_value2")

        self.assertEqual(query_string, "test1=test_1&test2=test_value2")
