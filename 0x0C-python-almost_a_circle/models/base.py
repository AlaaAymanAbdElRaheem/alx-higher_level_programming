#!/usr/bin/python3
"""defining Base class"""


import json
import csv


class Base:
    """implement Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """inistializing the class"""
        if id:
            Base.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + '.json'

        with open(filename, 'w', encoding='utf-8') as f:
            list_of_dic = []
            if list_objs:
                for obj in list_objs:
                    list_of_dic.append(obj.to_dictionary())
            f.write(cls.to_json_string(list_of_dic))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2)
        elif cls.__name__ == "Square":
            dummy = cls(2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + '.json'
        list_of_inst = []

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = cls.from_json_string(f.read())
            for elm in data:
                list_of_inst.append(cls.create(**elm))
        except FileNotFoundError:
            pass

        return list_of_inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string representation of list_objs to a file"""
        filename = cls.__name__ + '.csv'

        with open(filename, 'w', encoding='utf-8') as f:
            list_of_dic = []
            if list_objs:
                if cls.__name__ == "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                else:
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                for obj in list_objs:
                    list_of_dic.append(obj.to_dictionary())
                for o in list_of_dic:
                    writer.writerow(o)

    @classmethod
    def load_from_file_csv(cls):
        """Retuens list of instances from CSV file"""
        filename = cls.__name__ + ".csv"
        list_of_inst = []

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for elm in reader:
                    dic = {k: int(v) for k, v in elm.items()}
                    list_of_inst.append(cls.create(**dic))
        except FileNotFoundError:
            pass

        return list_of_inst
