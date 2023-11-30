#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models import *


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            return {
                key: value for key, value in FileStorage.__objects.items()
                if isinstance(value, cls)
                }
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:

            temp = {
                key: val.to_dict() for key,
                val in FileStorage.__objects.items()
            }

            json.dump(temp, f, indent=4)

    def delete(self, obj=None):
        """ Deletes an object from the storage dict """
        if obj is None:
            return
        else:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    def reload(self):
        """Loads storage dictionary from file"""

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            data = {}
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, val in data.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
