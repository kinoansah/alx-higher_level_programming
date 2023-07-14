# #!/usr/bin/python3
# """Defines unittests for base.py

# Unittest classes:
#     TestBase_instantiation - line 21
#     TestBase_to_json_string - line 108
#     TestBase_load_from_file_csv - line 482
#     TestBase_save_to_file_csv - line 404
#     TestBase_load_from_file - line 338
#     TestBase_create - line 286
#     TestBase_from_json_string - line 232
#     TestBase_save_to_file - line 154
# """
# import os
# import unittest
# from models.base import Base
# from models.rectangle import Rectangle
# from models.square import Square


# class TestBase_instantiation(unittest.TestCase):
#        """Unittests for testing instantiation of the Base class."""

#        def test_no_arg(self):
#            b1 = Base()
#            b2 = Base()
#            self.assertEqual(b1.id, b2.id - 1)

#        def test_three_bases(self):
#            b1 = Base()
#            b2 = Base ()
#            b3 = Base ()
#            self.assertEqual(b1.id, b3.id - 2)

#        def test_None_id(self):
#            b1 = Base(None)
#            b2 = Base(None)
#            self.assertEqual(b1.id, b2.id - 1)

#        def test_unique_id(self):
