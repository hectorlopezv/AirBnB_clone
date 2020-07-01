#!/usr/bin/python3
"""unit test for base_model"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import re


def reset_storage():
    """is reset_storage"""
    FileStorage._FileStorage__objects = {}
    if os.path.isfile(FileStorage._FileStorage__file_path):
        os.remove(FileStorage._FileStorage__file_path)


class TestBaseModel(unittest.TestCase):
    """unit test for base_model"""

    def setUp(self):
        """set up"""
        pass

    def tearDown(self):
        """tearDown"""
        pass

    def test_attribute(self):
        """test attribute"""
        attributes = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime}
        b = BaseModel()
        for k, v in attributes.items():
            self.assertTrue(hasattr(b, k))
            self.assertEqual(type(getattr(b, k, None)), v)

    def test_instance(self):
        """test instace creation"""

        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertEqual(str(type(b)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(b), BaseModel))
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.to_dict(), my_model.to_dict())

    def test_init(self):
        """test init"""
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_datetime_created(self):
        """test datetime"""
        date_now = datetime.now()
        b = BaseModel()
        diff = b.updated_at - b.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = b.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_str(self):
        """testing str"""
        b = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(str(b))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), b.id)
        s = res.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        d = json.loads(s.replace("'", '"'))
        d2 = b.__dict__.copy()
        d2["created_at"] = repr(d2["created_at"])
        d2["updated_at"] = repr(d2["updated_at"])
        self.assertEqual(d, d2)

    def test_id(self):
        """test id"""
        b = BaseModel()
        self.assertRegex(b.id, r'\w+-\w+-\w+-\w+-\w+')

    def test_to_dict(self):
        """testing to_dict method"""
        b = BaseModel()
        b.name = "holberton"
        b.age = 25
        dict_ = b.to_dict()
        self.assertEqual(dict_["id"], b.id)
        self.assertEqual(dict_["__class__"], type(b).__name__)
        self.assertEqual(dict_["created_at"], b.created_at.isoformat(sep=' '))
        self.assertEqual(dict_["updated_at"], b.updated_at.isoformat(sep=' '))
        self.assertEqual(dict_["name"], b.name)
        self.assertEqual(dict_["age"], b.age)

    def test_save_(self):
        """testing save"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        with open("file.json", "r") as f:
            read_ = json.load(f)
        self.assertRegex(str(read_), r'BaseModel.\w+-\w+-\w+-\w+-\w+')
        self.assertRegex(str(read_), r'{.+}')
        reset_storage()


if __name__ == '__main__':
    unittest.main()
