#!/usr/bin/python3
"""defining Base class"""


import json


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
            return []
        return json.dumps(list_dictionaries)

    @staticmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + '.json'

        if not list_objs:
            list_of_dic = []
        else:
            with open(filename, 'w', encoding='utf-8') as f:
                list_of_dic = []
                for obj in list_obj:
                    list_of_dic.append(obj.to_dictionary())
        f.write(cls.to_json_string(list_of_dic))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
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
        except FileNotFound:
            pass

        return list_of_inst
