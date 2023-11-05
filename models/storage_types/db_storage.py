#!/usr/bin/python3
""" Database storage implementation for all KYM data models. """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.movie import Movie
from models.cast import Cast
from models.user import User
from models.review import Review
import os

class DBStorage:
    """ Implements database storage for KYM data models. """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializes database storage parameters. """
        user = os.getenv('KYM_USER')
        pwd = os.getenv('KYM_PWD')
        host = os.getenv('KYM_HOST')
        name = os.getenv('KYM_DB')
        DATABASE_URL = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
            user, pwd, host, name
        )
        self.__engine = create_engine(
            DATABASE_URL,
            pool_pre_ping=True
        )
    
    def new(self, instance=None):
        """
        Adds instance to database storage.

        Arguments:
            - instance: An individual class object.
        """
        if instance is not None:
            try:
                self.__session.add(instance)
                self.__session.flush()
                self.__session.refresh(instance)
            except Exception:
                self.__session.rollback()
                raise Exception

    def save(self):
        """ Commits session changes. """
        self.__session.commit()
    
    def all(self, cls=None):
        """
        Returns all the instances of all classes
        or all the instances of a class in database storage.

        Arguments:
            - cls: class.
        """
        objects = {}
        classes = [Movie, Cast, User, Review]
        if cls is None:
            for clss in classes:
                query = self.__session.query(clss)
                for instance in query.all():
                    instance_key = '{}.{}'.format(instance.__class__.__name__, instance.id)
                    objects[instance_key] = instance
        else:
            query = self.__session.query(cls)
            for instance in query.all():
                instance_key = '{}.{}'.format(instance.__class__.__name__, instance.id)
                objects[instance_key] = instance
        return objects
    
    def delete(self, instance=None):
        """
        Removes instance from database storage.

        Arguments:
                - instance: An individual class object.
        """
        if instance is not None:
            self.__session.query(type(instance)).filter(
                type(instance).id == instance.id
            ).delete(synchronize_session=False)
        
    def load(self):
        """ Loads database storage. """
        Base.metadata.create_all(self.__engine)
        SessionFactory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        self.__session = scoped_session(SessionFactory)()
    
    def close(self):
        """ Closes database storage session. """
        self.__session.close()
