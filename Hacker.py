"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Hacker:


    def __init__(self,name):
            from Asset import Asset
            self.__name = name
            self.__inventory = []
            self.__trace = 0
            self.__rig = []
            self.__exposed = False
            self.add_asset_to_inventory(Asset("CryptoToken", "Used to acquire or repair rigs"), 1)

    def __str__(self):
        if self.__inventory:
            assets_str = "\n".join(
                f"{a.get_name().upper()} : {a.get_description()} (Qty: {a.get_quantity()})"
                for a in self.__inventory
            )

        else:
            assets_str = "No assets currently in inventory."

        if self.__rig:
                rig_str = "\n".join(
                    f"{r.get_name()}"
                    for r in self.__rig
                )
        else:
                rig_str = "None"



        return (
            f"**************\n"
            f"{self.__name.upper()}\n"
            f"**************\n"
            f"Owns Rig: {rig_str}\n"
            f"Current Trace Level: {self.__trace}\n"
            f"Current Assets:\n"
            f"{assets_str}"
        )

    def increase_trace(self):
        self.__trace += 1
        if self.__trace > 4:
            self.__exposed = True


    def get_inventory(self):
        return self.__inventory

    def add_asset_to_inventory(self,name,quantity):
            for p in self.__inventory:
                if p.get_name() == name.get_name():
                    p.increase_quantity(quantity)
                    print("Asset type already exists")
                    break
            else:
                self.__inventory.append(name)
                print("Asset type added to inventory")


    def acquire_rig(self,name):
        if self.__rig:
            print("Rig already acquired")  # Do nothing, rig already acquired

        else:
            for p in self.__inventory:                              #find the cryptotoken in inventory, and make sure greater than 1.
                if p.get_name() == "CryptoToken":
                    if p.get_quantity() >0:
                        self.__rig.append(name)
                        print(f"Rig {name.get_name()} acquired")    #add rig to the rig list
                        p.decrease_quantity(1)                      #spend 1 crypto token
                        if p.get_quantity() == 0:
                            self.scan_and_remove("CryptoToken")     #if 0 tokens left, remove from inventory

    def launch_data_spike(self,target):
        if self.__exposed:
            print(f"Cannot attack - trace level too high")
        else:
            for p in self.__rig:
                for k in p.get_storage():
                    if k.get_name() == "Data Spike":
                        if k.get_quantity() > 0:
                            k.decrease_quantity(1)
                            print(f"Data Spike launched at target {target.get_name()}")
                            target.increase_damage()
                            self.increase_trace()
                        else:
                            print(f"Not enough data spikes to launch attack")

    def extract_unsecured_assets(self,target):
        for k in self.__inventory:
            print(k.get_name())
            if k.get_name() == "Removable Drive":
                if k.get_quantity() > 0:
                    k.decrease_quantity(1)  # consume removable drive
                    for p in target.get_storage():
                        if p.get_encrypted() == False:  # asset not encrypted, transfer it
                            print(f"Asset {p.get_name()} extracted from inventory. Quantity: {p.get_quantity()}")
                            self.add_asset_to_inventory(p, p.get_quantity())
                            target.remove_asset_from_storage(p)
                            self.increase_trace()
                        else:
                            print(f"Could not extract {p.get_name()}, it is encrypted")
                else:
                    print(f"Not enough removable drives to extract assets")
        else:
            print(f"No drives in inventory")

    def encrypt_decrypt_asset(self, name, location, function):
        for k in self.__inventory:
            if k.get_name() == "Security Chip":
                if k.get_quantity() > 0:
                    if location == "Rig":
                        for p in self.__rig:
                            for y in p.get_storage():
                                if y.get_name() == name:
                                    if function == "Encrypt":
                                        if y.get_encrypted() == True:
                                            print(f"Asset already encrypted")
                                        else:
                                            y.set_encrypted(True)
                                            print(f"Asset {y.get_name()} encrypted in Rig")
                                            k.decrease_quantity(1)
                                    elif function == "Decrypt":
                                        if y.get_encrypted() == False:
                                            print(f"Asset not currently encrypted")
                                        else:
                                            y.set_encrypted(False)
                                            print(f"Asset {y.get_name()} decrypted in Rig")
                                            k.decrease_quantity(1)
                    elif location == "Hacker":
                        for p in self.__inventory:
                            if p.get_name() == name:
                                if function == "Encrypt":
                                    if p.get_encrypted() == True:
                                        print(f"Asset already encrypted")
                                    else:
                                        p.set_encrypted(True)
                                        print(f"Asset {p.get_name()} encrypted in Inventory")
                                        k.decrease_quantity(1)
                                elif function == "Decrypt":
                                    if p.get_encrypted() == False:
                                        print(f"Asset not currently encrypted")
                                    else:
                                        p.set_encrypted(False)
                                        print(f"Asset {p.get_name()} decrypted in Inventory")
                                        k.decrease_quantity(1)
                else:
                    print(f"Not enough security chips to encrypt or decrypt assets")
            else:
                print(f"No security chips in inventory")


    def upgrade_rig(self):
        for k in self.__inventory:
            if k.get_name() == "Hardware Patch":
                if k.get_quantity() > 0:
                    for p in self.__rig:
                        p.inc_upgrade_level()
                        k.decrease_quantity(1)
                else:
                    print(f"Not enough hardware patches to upgrade assets")
            else:
                print(f"No hardware patches in inventory")


    def move_asset_to_rig(self,name,quantity):
        for p in self.__inventory:
            if p.get_name() == name:
                if p.get_quantity() >= quantity:
                    for y in self.__rig:
                        for k in y.get_storage():
                            if k.get_name() == name:
                                k.set_quantity(k.get_quantity() + quantity)
                                print(f"{quantity} x {name} moved to Rig")
                                break
                            else:
                                y.append(name)
                                print(f"{quantity} x {name} moved to Rig")
                            p.set_quantity(p.get_quantity() - quantity)
                else:
                    print(f"Not enough assets available to move this quantity")
            else:
                print(f"Not enough assets available to move this quantity")



    def move_asset_to_inventory(self,name,quantity):
        for k in self.__rig:
            for p in k.get_storage():
                if p.get_name() == name:
                    if p.get_quantity() >= quantity:
                        for y in self.__inventory:
                            if y.get_name() == name:
                                set_quantity(y.get_quantity() + quantity)
                                print(f"{quantity} x {name} moved to Inventory")
                            else:
                                y.append(name)
                                print(f"{quantity} x {name} moved to Inventory")
                    else:
                        print(f"Not enough assets available to move this quantity")
                else:
                    print(f"Not enough assets available to move this quantity")


    def scan_and_remove(self,name):
        for k in self.__inventory:
            if k.get_name() == name:
                self.__inventory.remove(k)

    def repair_rig(self):
        for p in self.__inventory:
            if p.get_name() == "CryptoToken":
                if p.get_quantity() > 0:
                    for k in self.__rig:
                        k.repair_rig()
                else:
                    print(f"Not enough crypto tokens to repair rig")
            else:
                print(f"No crypto tokens in inventory")
