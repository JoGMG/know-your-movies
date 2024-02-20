#!/usr/bin/python3
""" Base model which all KYM data models inherit from. """
from sqlalchemy import Column, String, Integer, ForeignKey, DATETIME
from sqlalchemy.orm import declarative_base, relationship
import uuid
import os
from datetime import datetime

Base = declarative_base()

class BaseModel:
    """ Base class for all KYM classes. """
    id = Column(String(64), nullable=False, primary_key=True, unique=True)

    def __init__(self, *args, **kwargs):
        """
        Initializes new instance attribute(s).

        Arguments:
            - kwargs: key, value arguments passed.
        """
        for key, value in kwargs.items():
            if key != '__class__':
                setattr(self, key, value)

        if 'id' not in kwargs:
            setattr(self, 'id', str(uuid.uuid4()))

        from models.review import Review
        if isinstance(self, Review):
            if 'date' not in kwargs:
                setattr(self, 'date', datetime.utcnow())

        from models.user import User
        if isinstance(self, User):
            if 'name' not in kwargs:
                email = kwargs.get('email')
                if email is None:
                    return
                name = email.partition('@')
                setattr(self, 'name', name[0])

    def __str__(self):
        """ Returns string representation. """
        cls = self.__class__.__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def to_dict(self):
        """ Converts instance representation to json format. """
        json_format = {}
        for key, value in self.__dict__.items():
            if key != '_sa_instance_state':
                if isinstance(value, datetime):
                    json_format[key] = value.isoformat()
                else:
                    json_format[key] = value
        json_format['__class__'] = self.__class__.__name__
        return json_format
