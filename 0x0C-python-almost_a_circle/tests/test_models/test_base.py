import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test case for the Base class."""

    def test_base(self):
        """
        Test the functionality of the Base class.

        Steps:
        1. Create a Base instance with id=10.
        2. Verify that the id attribute is set to 10.
        3. Reset the __nb_objects attribute to 0.
        4. Create two more Base instances without specifying id.
        5. Verify that the id attributes are assigned incrementally.

        """
        base_instance = Base(id=10)
        self.assertEqual(base_instance.id, 10)
        Base._Base__nb_objects = 0

        base_instance_1 = Base()
        base_instance_2 = Base()
        self.assertEqual(base_instance_1.id, 1)
        self.assertEqual(base_instance_2.id, 2)


if __name__ == '__main__':
    unittest.main()
