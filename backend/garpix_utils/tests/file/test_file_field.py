from datetime import date

from rest_framework.test import APITestCase

from garpix_utils.file.file_field import get_file_path, UploadTo


class GetFilePath(APITestCase):
    def setUp(self) -> None:
        today = date.today()
        self.filenames = [
            (
                f"__ utils.__file{i}.txt",
                f"uploads/{today.year}/{today.month}/utils-file{i}.txt",
            )
            for i in range(3)
        ]
    
    def test_get_file_path(self) -> None:
        for filename, return_ in self.filenames:
            self.assertEqual(get_file_path(None, filename), return_)


class UploadToTest(APITestCase):
    def setUp(self) -> None:
        today = date.today()
        self.upload = UploadTo("test")
        self.filenames = [
            (
                type(f"instance{i}", (object,), {})(),
                f"_-- utils.--file{i}.txt",
                f"uploads/instance{i}/test/{today.year}/{today.month}/utils-file{i}.txt",
            )
            for i in range(3)
        ]
    
    def test_upload_to(self) -> None:
        for instance, filename, return_ in self.filenames:
            self.assertEqual(self.upload(instance, filename), return_)
    
    def test_deconstruct(self) -> None:
        return_ = ("garpix_utils.file.UploadTo", "test", {})
        self.assertEqual(self.upload.deconstruct(), return_)
