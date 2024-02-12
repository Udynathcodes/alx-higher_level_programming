"""Rectangle units tests"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
    Test suite for the Rectangle class, a subclass of the Base class,
    which represents rectangles with width, height, and optional x,
    y coordinates.
    """

    def test_if_subclass(self):
        """
        Test if Rectangle is a subclass of Base.
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_2_args(self):
        """
        Test the creation of a Rectangle with two arguments
        (width and height).
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, Base._Base__nb_objects)

    def test_1_arg(self):
        """
        Test that a TypeError is raised when trying to create
        a Rectangle with only one argument.
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(10)

    def test_no_args(self):
        """
        Test that a TypeError is raised when trying to create
        a Rectangle with no arguments.
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_many_args(self):
        """
        Test the creation of a Rectangle with multiple arguments
        (width, height, x, y, and id).
        """
        r1 = Rectangle(10, 2, 4, 5, 9)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 9)

    def test_errors(self):
        """
        Test method to verify that the Rectangle class
        correctly raises specific
        errors (TypeError or ValueError) with appropriate
        error messages
        during instance creation and attribute setting.

        The following scenarios are covered:
        1. Creating a Rectangle with a non-integer width
        raises TypeError
        with the message "width must be an integer".
        2. Creating a Rectangle with a non-integer height
        raises TypeError
        with the message "height must be an integer".
        3. Creating a Rectangle with a negative width raises
        ValueError
        with the message "width must be > 0".
        4. Creating a Rectangle with a negative height raises
        ValueError
        with the message "height must be > 0".
        5. Creating a Rectangle with a negative x-coordinate
        raises ValueError
        with the message "x must be >= 0".
        6. Creating a Rectangle with a negative y-coordinate
        raises ValueError
        with the message "y must be >= 0".
        """
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle("10", 2)
        err_msg = "width must be an integer"
        self.assertEqual(str(e.exception), err_msg)

        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(10, "2")
        err_msg = "height must be an integer"
        self.assertEqual(str(e.exception), err_msg)

        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(-1, 2)
        err_msg = "width must be > 0"
        self.assertEqual(str(e.exception), err_msg)

        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(1, -2)
        err_msg = "height must be > 0"
        self.assertEqual(str(e.exception), err_msg)

        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(1, 2, -1)
        err_msg = "x must be >= 0"
        self.assertEqual(str(e.exception), err_msg)

        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(1, 2, 3, -4)
        err_msg = "y must be >= 0"
        self.assertEqual(str(e.exception), err_msg)

    def test_area(self):
        """Test method to confirm the area of the Rectangle"""
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.area(), 50)

    def test_char_area(self):
        """Test method for Rectangle instance with the character #"""
        r1 = Rectangle(2, 3)
        char = "##\n##\n##\n"
        self.assertEqual(r1.display(), char)

    def test_str_2args(self):
        """Test __str__ method with 2 arguments"""
        r1 = Rectangle(4, 2)
        output = f'[Rectangle] ({Base._Base__nb_objects}) 0/0 - 4/2'
        self.assertEqual(str(r1), output)

    def test_str_no_id(self):
        """Test __str__ method without id parameter"""
        r1 = Rectangle(5, 6, 1, 2)
        output = f'[Rectangle] ({Base._Base__nb_objects}) 1/2 - 5/6'
        self.assertEqual(str(r1), output)

    def test_str_all_args(self):
        """Test __str__ with all arguments"""
        r1 = Rectangle(3, 5, 2, 1, 15)
        output = f'[Rectangle] (15) 2/1 - 3/5'
        self.assertEqual(str(r1), output)

    def test_dict_2args(self):
        """
        Test the dictionary representation of a Rectangle
            with only 2 arguments
        """
        r1 = Rectangle(2, 3)
        dict = {'x': 0, 'y': 0, 'id': Base._Base__nb_objects,
                'height': 3, 'width': 2}
        self.assertEqual(r1.to_dictionary(), dict)

    def test_dict_all_args(self):
        """
        Test the dictionary representation of a Rectangle
            with all arguments
        """
        r1 = Rectangle(2, 3, 4, 5, 6)
        dict = {'x': 4, 'y': 5, 'id': 6, 'height': 3, 'width': 2}
        self.assertEqual(r1.to_dictionary(), dict)


if __name__ == "__main__":
    unittest.main()
