#!/usr/bin/python3
"""Base class to inherit from"""

from datetime import datetime
import uuid


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initializes the Base model class attributes
        Args:
            id - identification number
            *args - will not be used
            **kwargs - dictionary arguments
        """
        from models import storage

        if kwargs and kwargs is not {}:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v,
                                                       "%Y-%m-%dT%H:%M:%S.%f"))
                elif k == "__class__":
                    continue
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return strings of class name, id and dictionary of attributes"""

        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """update updated_at with the current datetime"""
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns all keys/values of __dict__ of the instance"""

        d = self.__dict__.copy()
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()

        return d
