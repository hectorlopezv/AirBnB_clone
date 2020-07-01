#!/usr/bin/python3
"""base class """

import uuid
from datetime import datetime


class BaseModel:

    """Class for base model of object hierarchy."""

    def __init__(self, *args, **kwargs):
        """Initialization of a Base instance."""
        if not kwargs:
            from models import storage

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            self.__dict__.update(kwargs)
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            del self.__dict__["__class__"]


    def __str__(self):
        """Returns a human-readable string representation
        of an instance."""

        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute
        with the current datetime."""
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an instance."""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
