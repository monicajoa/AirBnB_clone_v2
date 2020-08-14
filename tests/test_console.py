#!/usr/bin/python3

import unittest
import console
import pep8


HBNBCommand = console.HBNBCommand


class TestConsole(unittest.TestCase):

    def test_prompt(self):
        self.assertEqual("(hbnb)", HBNBCommand.prompt)

    def test_console_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["./console.py"])
        self.assertEqual(result.total_error, 0)

    def test__file_console_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["./console.py"])
        self.assertEqual(result.total_error, 0)

    def test_class_console_docstring(self):
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand without documentation")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand without documentation")

    def test_console_docstring(self):
        self.assertIsNot(console.__doc__, None,
                         "Console.py without documentation")
        self.assertTrue(len(console.__doc__) >= 1,
                        "Console.py without documentation")
