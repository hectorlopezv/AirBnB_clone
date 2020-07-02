#!/usr/bin/python3
"""Module for FileStorage class."""
import json


class FileStorage:

    """Class for serializtion and deserialization of base classes."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dictionary of objects"""
        return FileStorage._FileStorage__objects

    def new(self, obj):
        """add new objecto to dictionary"""
        FileStorage._FileStorage__objects[str(
            obj.__class__.__name__) + '.' + obj.id] = obj

    def save(self):
        """dict_ to json_format"""
        with open(self.__file_path, 'w') as f2:
            dict_ = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dict_, f2)

    def accepted_classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """json to -> _FileStorage__objects"""
        classes = self.accepted_classes()
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                dict_ = json.load(f)
                dict_ = {k: classes[v["__class__"]]
                         (**v) for k, v in dict_.items()}
                FileStorage._FileStorage__objects.update(dict_)
        except BaseException:
            pass
