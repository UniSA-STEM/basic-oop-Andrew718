"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Asset:

    def __init__(self,name,description):
            self.__name = name
            self.__description = description
            self.__quantity = 0
            self.__encrypted = False

    def __str__(self):
            return (
                f"{self.__name.upper()} : {self.__description}\n"
            )

    def get_quantity(self):
        return self.__quantity

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_encrypted(self):
        return self.__encrypted

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_name(self, name):
        self.__name = name

    def set_description(self, description):
        self.__description = description

    def set_encrypted(self, status):
        self.__encrypted = status

    def increase_quantity(self,quantity):
        self.__quantity  = self.__quantity + quantity


    def decrease_quantity(self,quantity):
        self.__quantity  = self.__quantity - quantity