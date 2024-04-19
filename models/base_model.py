#!/usr/bin/python3
""" Base model which all KYM data models inherit from. """
from sqlalchemy import Column, String, Integer, ForeignKey, DATETIME, Date
from sqlalchemy.orm import declarative_base, relationship
import uuid
import os
from datetime import datetime, date

Base = declarative_base()


class BaseModel:
    """ Base class for all KYM classes. """
    id = Column(String(64), nullable=False, primary_key=True, unique=True)
    created_at = Column(DATETIME, default=datetime.utcnow())
    updated_at = Column(DATETIME, default=datetime.utcnow())

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

        if 'created_at' not in kwargs:
            setattr(self, 'created_at', datetime.utcnow())

        if 'updated_at' not in kwargs:
            setattr(self, 'updated_at', datetime.utcnow())

        from models.user import User
        if isinstance(self, User):
            if 'author' not in kwargs or not kwargs.get('author'):
                email = kwargs.get('email', None)
                if email is None:
                    return
                author = email.partition('@')
                setattr(self, 'author', author[0])

        from models.movie import Movie
        if isinstance(self, Movie):
            release_date = kwargs.get('release_date')
            if release_date:
                year = release_date.partition('-')[0]
                month = release_date.partition('-')[2].partition('-')[0]
                day = release_date.partition('-')[2].partition('-')[2]
                if os.getenv('KYM_STORAGE') == 'db':
                    release_date_obj = date(int(year), int(month), int(day))
                else:
                    release_date_obj = str(date(
                        int(year), int(month), int(day)))
                setattr(self, 'release_date', release_date_obj)
        
        from models.review import Review
        if isinstance(self, Review):
            content = kwargs.get('content')
            if content:
                str_content = str(content).strip()
                setattr(self, 'content', str_content)

    def __str__(self):
        """ Returns string representation. """
        cls = self.__class__.__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """ Stores instance to storage """
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ Converts instance representation to json format. """
        json_format = {}
        for key, value in self.__dict__.items():
            if key != '_sa_instance_state':
                if isinstance(value, datetime):
                    json_format[key] = value.isoformat()
                elif isinstance(value, date) or key == 'content':
                    json_format[key] = str(value)
                else:
                    json_format[key] = value
        json_format['__class__'] = self.__class__.__name__
        return json_format

    def delete(self):
        """ Deletes instance from storage """
        from models import storage
        storage.delete(self)
