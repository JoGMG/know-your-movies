#!/usr/bin/python3
""" File storage implementation for all KYM data models. """
from models.movie import Movie
from models.cast import Cast
from models.user import User
from models.review import Review
import json
import os

classes = {
    "Movie": Movie, "Cast": Cast,
    "User": User, "Review": Review
}

class FileStorage:
    """ Implements file storage for KYM data models. """
    __file_path = 'file.json'
    __objects = {}

    def new(self, instance=None):
        """
        Adds instance to __objects (file storage dictionary).

        Arguments:
            - instance: An individual class object.
        """
        if instance is not None:
            self.__objects.update(
                {instance.to_dict()['__class__'] + '.' + instance.id: instance}
            )

    def save(self):
        """ Save added instances to file storage (file.json). """
        with open(self.__file_path, 'w') as file:
            temp = {}
            for key, value in self.__objects.items():
                temp[key] = value.to_dict()
            json.dump(temp, file)

    def all(self, cls=None):
        """
        Returns all the instances of all classes or all the instances of
        a class in file storage (file.json).

        Arguments:
            - cls: class.
        """
        if cls is None:
            return self.__objects
        else:
            cls_instances = {}
            for key, value in self.__objects.items():
                if type(value) is cls:
                    cls_instances[key] = value
            return cls_instances

    def delete(self, instance=None):
        """
        Removes instance from __objects (file storage dictionary).

        Arguments:
                - instance: An individual class object.
        """
        if instance is not None:
            instance_key = instance.to_dict()['__class__'] + '.' + instance.id
            if instance_key in self.__objects.keys():
                del self.__objects[instance_key]

    def load(self):
        """
        Loads stored objects in file storage (file.json)
        to __objects (file storage dictionary).
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                temp = json.load(file)
                for key, value in temp.items():
                    self.__objects[key] = classes[value['__class__']](**value)

    def close(self):
        """ Closes storage. """
        self.load()
