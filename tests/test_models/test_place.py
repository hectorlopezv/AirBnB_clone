#!/usr/bin/python3
"""unit test for user classes."""

import unittest
from models.engine.file_storage import FileStorage
from models.user import User
import os
import json
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """unit testing for test user"""

    def tearDown(self):
        """tear"""
        pass

    def setUp(self):
        """set up"""
        pass

    def test_instance_creation(self):
        """test instance creation"""
        b = Place()
        self.assertEqual(str(type(b)), "<class 'models.place.Place'>")
        self.assertIsInstance(b, Place)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_attribute(self):
        """test correct attributes"""
        b = Place()
        attr_ = {"city_id": str,
                 "user_id": str,
                 "name": str,
                 "description": str,
                 "number_rooms": int,
                 "number_bathrooms": int,
                 "max_guest": int,
                 "price_by_night": int,
                 "latitude": float,
                 "longitude": float,
                 "amenity_ids": list}
        for k, v in attr_.items():
            self.assertTrue(hasattr(b, k))
            self.assertEqual(type(getattr(b, k, None)), v)


if __name__ == "__main__":
    unittest.main()
