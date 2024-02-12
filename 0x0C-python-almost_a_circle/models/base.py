#!/usr/bin/python3
"""Modules imported"""
import json
import csv


class Base:
    """Base class for managing id attribute in future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Parameters:
        - id (int or None): If provided, assigns the id attribute
        with the given value.
                    If None, increments __nb_objects and
                    assigns the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Method that returns the JSON string
        representation of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that writes the JSON string representation
        of list_objs to a file
        """
        new_list_obj = []
        if list_objs is not None:
            for obj in list_objs:
                new_list_obj.append(obj.to_dictionary())

            j_data = cls.to_json_string(new_list_obj)
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(j_data)

    @staticmethod
    def from_json_string(json_string):
        """
        static method that returns the list of
        the JSON string representation json_string
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Class method that returns an instance with all
        attributes already set
        """
        from models.square import Square
        from models.rectangle import Rectangle
        if cls is Square:
            d_cls = Square(4)
        elif cls is Rectangle:
            d_cls = Rectangle(3, 4)

        d_cls.update(**dictionary)
        return d_cls

    @classmethod
    def load_from_file(cls):
        """
         class method that returns a list of instances
        """
        filename = "{}.json".format(cls.__name__)

        try:
            with open(filename, "r", encoding="utf-8") as file:
                read_data = file.read()
        except FileNotFoundError:
            return []

        data_list = cls.from_json_string(read_data)
        instances_list = [cls.create(**data) for data in data_list]
        return instances_list

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves to csv"""
        if list_objs is not None:
            filename = "{}.csv".format(cls.__name__)
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Loads from csv"""
        created_instances = []
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                row = [int(r) for r in row]
                if cls.__name__ == "Rectangle":
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                elif cls.__name__ == "Square":
                    d = {"id": row[0], "size": row[1], "x": row[2],
                         "y": row[3]}
                created_instances.append(cls.create(**d))
        return created_instances
