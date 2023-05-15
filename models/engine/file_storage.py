#!/usr/bin/python3
"""serializes instances
to a JSON file and deserializes JSON file to instances
"""

import json
from models.user import User
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import os


class FileStorage:
    """serializes instances to a
    JSON file and deserializes JSON file to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns dictionary __object"""

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        Args:
           obj - the class type
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        tmp_dict = {}
        for k, v in self.__objects.items():
            tmp_dict[k] = v.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as written_file:
            json.dump(tmp_dict, written_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        dict_of_dicts = {}
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State}

        try:
            temp_dict = {}
            with open(self.__file_path, "r") as r:
                dict_of_dicts = json.load(r)
            for k, v in dict_of_dicts.items():
                if v['__class__'] in classes:
                    temp_dict[k] = classes[v['__class__']](**v)
            self.__objects = temp_dict
        except Exception:
            pass
