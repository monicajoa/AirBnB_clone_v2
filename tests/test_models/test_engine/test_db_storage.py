#!/usr/bin/python3

import unittest
import pep8
import MySQLdb
from os import getenv


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "Storage should be db")
def test_bd_storage_pep8(self):
    pep8style = pep8.StyleGuide(quiet=True)
    result = pep8style.check_files(["./models/engine/db_storage.py"])
    self.assertEqual(result.total_error, 0)
