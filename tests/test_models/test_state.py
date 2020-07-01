#!/usr/bin/python3
"""unit test for user classes."""

import unittest
from models.engine.file_storage import FileStorage
from models.user import User
import os
import json
from datetime import datetime
from models.base_model import BaseModel
from models.state import State


class TestReview(unittest.TestCase):
    """unit testing for test user"""

    def tearDown(self):
        """tear"""
        pass

    def setUp(self):
        """set up"""
        pass

    def test_instance_creation(self):
        """test instance creation"""
        b = State()
        self.assertEqual(str(type(b)), "<class 'models.state.State'>")
        self.assertIsInstance(b, State)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_attribute(self):
        """test correct attributes"""
        b = State()
        attr_ = {"name": str}
        for k, v in attr_.items():
            self.assertTrue(hasattr(b, k))
            self.assertEqual(type(getattr(b, k, None)), v)


if __name__ == "__main__":
    unittest.main()
