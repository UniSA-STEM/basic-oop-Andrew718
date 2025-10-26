"""
File: Rig.py
Description: Rig Class
Author: Andrew Watt
ID: 110352236
Username: WATAY024
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import random
from Asset import Asset

class Rig:

    def __init__(self, name):
        self.__name = name
        self.__storage = []
        self.__damage = 0
        self.__broken = False
        self.__upgrade_level = 0
        self.add_asset_to_rig(Asset("Data Spike", "Used in battles"), 2)
        self.add_asset_to_rig(Asset("Removable Drive", "Found in rigs and used for extraction"), 1)

    def __str__(self):
        if self.__storage:
            # Join each asset’s string representation with newlines
            storage_str = "\n".join(
                f"{a.get_name().upper()} : {a.get_description()} (Qty: {a.get_quantity()}) : <*ENCRYPTED: {a.get_encrypted()}*>"
                for a in self.__storage
            )
        else:
            storage_str = "No assets currently in inventory."
        return (
            f"Rig Name: {self.__name}\n"
            f"Current Damage: {self.__damage}\n"
            f"Condition: {self.rig_condition()}\n"
            f"Upgrade Level: {self.__upgrade_level}\n"
            f"Storage: \n{storage_str}\n"
        )




    def get_name(self):
        return self.__name

    def get_storage(self):
        return self.__storage

    def get_upgrade_level(self):
        return self.__upgrade_level

    def inc_upgrade_level(self):
        self.__upgrade_level = self.__upgrade_level + 1

    def add_asset_to_rig(self,name,quantity):
            for p in self.__storage:
                if p.get_name() == name:
                    p.increase_quantity(quantity)
                    print("Asset type already exists")
                    break
            else:
                self.__storage.append(name)
                name.increase_quantity(quantity)
                print("Asset type added to storage")


    def increase_damage(self):
            self.__damage += 1
            if self.__damage == 2:
                self.__broken = True
                print("Rig is broken!")


    def remove_asset_from_storage(self,name):
            self.__storage.remove(name)

    def repair_rig(self):
        self.__damage = 0
        self.__broken = False

    def rig_condition(self):
        condition_str = ""
        if self.__damage == 2:
            condition_str = "Broken"
        elif self.__damage == 1:
            condition_str = "OK"
        elif self.__damage == 0:
            condition_str = "Pristine"

        upgrade_str = ""
        if self.__upgrade_level == 0:
            upgrade_str = "Level 0"
        elif self.__upgrade_level == 1:
            upgrade_str = "Level 1"
        elif self.__condition == 2:
            upgrade_str = "Level 2"

        return(f"{condition_str} ({upgrade_str})")

    def generate_asset(self):
        generated = random.randint(0,4)
        if generated == 0:
            self.add_asset_to_rig(Asset("CryptoToken", "Used to acquire or repair rigs"), 1)
            print(f"Rig has generated 1 x Crypto Token and added to storage")
        if generated == 1:
            self.add_asset_to_rig(Asset("Data Spike", "Used in battles"), 2)
            print(f"Rig has generated 1 x Data Spike and added to storage")
        if generated == 2:
            self.add_asset_to_rig(Asset("Removable Drive", "Found in rigs and used for extraction"), 1)
            print(f"Rig has generated 1 x Removable Drive and added to storage")
        if generated == 3:
            self.add_asset_to_rig(Asset("Security Chip", "Used to encrypt or decrypt assets"), 1)
            print(f"Rig has generated 1 x Security Chip and added to storage")
        if generated == 4:
            self.add_asset_to_rig(Asset("Hardware Patch", "Used to upgrade rigs"), 1)
            print(f"Rig has generated 1 x Hardware Patch and added to storage")





