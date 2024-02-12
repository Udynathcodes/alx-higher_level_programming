"""Square units tests"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class SquareTest(unittest.TestCase):
    def test_if_subclass(self):
        """
        Test if Square is a subclass of Base.
        """
        self.assertTrue(issubclass(Square, Rectangle))

    def test_2_args(self):
        """
        Test the creation of a Square with two arguments
        (size and x).
        """
        s1 = Square(10, 2)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, Base._Base__nb_objects)

    def test_1_arg(self):
        """
        Test the creation of a square with 1 argument
        """
        s1 = Square(10)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, Base._Base__nb_objects)

    def test_no_args(self):
        """
        Test that a TypeError is raised when trying to create
        a Square with no arguments.
        """
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_many_args(self):
        """
        Test the creation of a Square with multiple arguments
        (size, x, y, and id).
        """
        s1 = Square(10, 2, 4, 5)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, 5)

    def test_str_2args(self):
        """Test __str__ method with 2 arguments"""
        s1 = Square(4, 2)
        output = f'[Square] ({Base._Base__nb_objects}) 2/0 - 4'
        self.assertEqual(str(s1), output)

    def test_str_no_id(self):
        """Test __str__ method without id parameter"""
        s1 = Square(5, 6, 1)
        output = f'[Square] ({Base._Base__nb_objects}) 6/1 - 5'
        self.assertEqual(str(s1), output)

    def test_str_all_args(self):
        """Test __str__ with all arguments"""
        s1 = Square(3, 5, 2, 15)
        output = f'[Square] (15) 5/2 - 3'
        self.assertEqual(str(s1), output)

    def test_errors(self):
        """
        Test suite for handling errors in Square initialization.

        This test ensures that appropriate errors are raised when
        invalid arguments are provided
        during the creation of a Square instance. It covers scenarios
        where non-integer values,
        negative values, or a combination of both are passed as
        arguments for size, x, or y.

        Test Cases:
        1. Raises a TypeError if a non-integer is passed as the size.
        2. Raises a ValueError if a negative value is passed as the
        size.
        3. Raises a ValueError if a negative value is passed as the
        x-coordinate.
        4. Raises a ValueError if a negative value is passed as the
        y-coordinate.
        """
        with self.assertRaises(TypeError) as e:
            s1 = Square("10")
        err_msg = "width must be an integer"
        self.assertEqual(str(e.exception), err_msg)

        with self.assertRaises(ValueError) as e:
            s1 = Square(-1)
        err_msg = "width must be > 0"
        self.assertEqual(str(e.exception), err_msg)

        with self.assertRaises(ValueError) as e:
            s1 = Square(1, -2)
        err_msg = "x must be >= 0"
        self.assertEqual(str(e.exception), err_msg)

        with self.assertRaises(ValueError) as e:
            s1 = Square(1, 2, -3)
        err_msg = "y must be >= 0"
        self.assertEqual(str(e.exception), err_msg)

    def test_dict_2args(self):
        """
        Test the dictionary representation of a Square
            with only 2 arguments
        """
        s1 = Square(2, 3)
        dict = {'id': Base._Base__nb_objects, 'x': 3, 'size': 2, 'y': 0}
        self.assertEqual(s1.to_dictionary(), dict)

    def test_dict_all_args(self):
        """
        Test the dictionary representation of a Square
            with all arguments
        """
        s1 = Square(2, 3, 4, 5)
        dict = {'id': 5, 'x': 3, 'size': 2, 'y': 4}
        self.assertEqual(s1.to_dictionary(), dict)
