#!/usr/bin/python3
"""unittests for console.py.
Unittest classes:
TestHBNBCommand_prompting
TestHBNBCommand_help
TestHBNBCommand_exit
TestHBNBCommand_create
TestHBNBCommand_show
TestHBNBCommand_all
TestHBNBCommand_destroy
TestHBNBCommand_update
"""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_prompting(unittest.TestCase):
	"""Unittests for testing prompting of the HBNB command interpreter."""

		def test_prompt_string(self):
			self.assertEqual("(hbnb) ", HBNBCommand.prompt)

			def test_empty_line(self):
				with patch("sys.stdout", new=StringIO()) as output:
					self.assertFalse(HBNBCommand().onecmd(""))
					self.assertEqual("", output.getvalue().strip())
					ass TestHBNBCommand_help(unittest.TestCase):
						"""Unittests for testing help messages of the HBNB command interpreter."""

							def test_help_quit(self):
								h = "Quit command to exit the program."
								with patch("sys.stdout", new=StringIO()) as output:
	self.assertFalse(HBNBCommand().onecmd("help quit"))
	self.assertEqual(h, output.getvalue().strip())

	def test_help_create(self):
		h = ("Usage: create <class>\n        "
				"Create a new class instance and print its id.")
		with patch("sys.stdout", new=StringIO()) as output:
	self.assertFalse(HBNBCommand().onecmd("help create"))
	self.assertEqual(h, output.getvalue().strip())


	class TestHBNBCommand_exit(unittest.TestCase):
		"""Unittests for testing exiting from the HBNB command interpreter."""

			def test_quit_exits(self):
				with patch("sys.stdout", new=StringIO()) as output:
					self.assertTrue(HBNBCommand().onecmd("quit"))

					def test_EOF_exits(self):
						with patch("sys.stdout", new=StringIO()) as output:
							self.assertTrue(HBNBCommand().onecmd("EOF"))



							class TestHBNBCommand_create(unittest.TestCase):
								"""Unittests for testing create from the HBNB command interpreter."""

									@classmethod
									def setUp(self):
										try:
										os.rename("file.json", "tmp")
										except IOError:
										pass
										FileStorage.__objects = {}

										@classmethod
										def tearDown(self):
											try:
											os.remove("file.json")
											except IOError:
											pass
											try:
											os.rename("tmp", "file.json")
											except IOError:
											pass

											def test_create_missing_class(self):
												correct = "** class name missing **"
												with patch("sys.stdout", new=StringIO()) as output:
	self.assertFalse(HBNBCommand().onecmd("create"))
	self.assertEqual(correct, output.getvalue().strip())


	class TestHBNBCommand_show(unittest.TestCase):
		"""Unittests for testing show from the HBNB command interpreter"""

			@classmethod
			def setUp(self):
				try:
				os.rename("file.json", "tmp")
				except IOError:
				pass
				FileStorage.__objects = {}

				@classmethod
				def tearDown(self):
					try:
					os.remove("file.json")
					except IOError:
					pass
					try:
					os.rename("tmp", "file.json")
					except IOError:
					pass

					class TestHBNBCommand_destroy(unittest.TestCase):
						"""Unittests for testing destroy from the HBNB command interpreter."""

							@classmethod
							def setUp(self):
								try:
								os.rename("file.json", "tmp")
								except IOError:
								pass
								FileStorage.__objects = {}

								@classmethod
								def tearDown(self):
									try:
									os.remove("file.json")
									except IOError:
									pass
									try:
									os.rename("tmp", "file.json")
									except IOError:
	pass
	    storage.reload()


if __name__ == "__main__":
    unittest.main()
