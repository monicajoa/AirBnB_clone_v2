#!/usr/bin/python3
""" This module defines a class to manage database storage for hbnb clone """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import models
from os import getenv


class DBStorage:
    """ Database Engine for Air bnb clone """
    __engine = None
    __session = None
    def __init__(self):
        """ Init method """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                       pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(engine)

    def all(self, cls=None):
        """ Return a dictionary of the class """
        dic = {}
        if cls:
            objects = self.__session.query(cls).all()
        else:
            objects = self.__session.query(models.State).all()
            objects += self.__session.query(models.City).all()
            objects += self.__session.query(models.User).all()
            objects += self.__session.query(models.Place).all()
            objects += self.__session.query(models.Amenity).all()
            objects += self.__session.query(models.Review).all()
        for obj in objects:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            dic[key] = obj
        return dic

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()
