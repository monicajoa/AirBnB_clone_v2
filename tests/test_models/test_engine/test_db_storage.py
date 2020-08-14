#!/usr/bin/python3

import unittest
import pep8
import MySQLdb
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.db_storage import DBStorage

class TestDBStorage(unittest.TestCase):
    """ This will test the DBStorage class """
    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "Storage should be db")
    def setUp(self):
        """ Set up for tests """
        self.db = MySQLdb.connect(host=getenv('HBNB_MYSQL_HOST'),
                                port=3306,
                                user=getenv('HBNB_MYSQL_USER'),
                                passwd=getenv('HBNB_MYSQL_USER'),
                                db=getenv('HBNB_MYSQL_DB'))
        cur = self.db.cursor()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "Storage should be db")
    def tearDown(self):
        """ At the end of every tests this will tear it down """
        self.cur.close()
        self.db.close()

    def test_bd_storage_pep8(self):
        """ Test code style """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["./models/engine/db_storage.py"])
        self.assertEqual(result.total_error, 0)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "Storage should be db")
    def test_attributes_DBStorage(self):
        """ Test the class attributes """
        self.assertTrue(hasattr(DBStorage, '_DBStorage__engine'))
        self.assertTrue(hasattr(DBStorage, '_DBStorage__session'))
        self.assertTrue(hasattr(DBStorage, 'all'))
        self.assertTrue(hasattr(DBStorage, 'new'))
        self.assertTrue(hasattr(DBStorage, 'save'))
        self.assertTrue(hasattr(DBStorage, 'delete'))
        self.assertTrue(hasattr(DBStorage, 'reload'))
