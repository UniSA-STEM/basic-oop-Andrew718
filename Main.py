"""
File: main.py
Description:  Main methods to be used in hacker simulation
Author: Andrew Watt
ID: 110352236
Username: WATAY024
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker
from Rig import Rig
from Asset import Asset

#assets are instantiated within the class init functions

#instantiate hackers

Morpheus = Hacker("Morpheus")
Trinity = Hacker("Trinity")

#instantiate rigs
Asus = Rig("Asus")
Dell: Rig = Rig("Dell")

#show initial status of hackers
print(Morpheus)
print(Trinity)

#Acquire rigs for Hackers
Morpheus.acquire_rig(Asus)
Trinity.acquire_rig(Dell)

#show initial state of rigs
print(Asus)
print(Dell)


# Launch data spike attack. Attack is targeted at the rig, not the hacker. Hacker may have multiple rigs in future
# Attack is blocked if trace level is too high
Morpheus.launch_data_spike(Dell)

#extract unencrypted assets from target rig. Consumes a removable drive and any encrypted assets will not be moved.
# if inventory has no drives, it will fail
Morpheus.extract_unsecured_assets(Dell)

#encrypt or decrypt an asset. Function takes arguments for the asset type, where you are wanting to encrypt it (Rig or Inventory) and whether to encrypt or decrypt
# Consumes a security chip for both encrypting and decrypting, and will fail if none exist in inventory.
# increases trace level by 1
Morpheus.encrypt_decrypt_asset("Data Spike", "Rig", "Encrypt")

# Upgrades the hackers rig - increases level by 1. Consumes a hardware patch and will fail if none exist in inventory
Morpheus.upgrade_rig()


#Functions to move assets between inventory and rigs. Checks to ensure there is enough quantity to move before going ahead.

Morpheus.move_asset_to_inventory("Data Spike",1)

Morpheus.move_asset_to_rig("Data Spike",1)

# Function to scan the inventory and remove an item

Morpheus.scan_and_remove("Data Spike")

#function to repair rig. Consumes hardware patch. If none available, will fail.
#sets broken status to false, and damage to 0
Morpheus.repair_rig()

# Function to manually add assets to rig. Used in init to create default rig storage
Asus.add_asset_to_rig("Data Spike",1)

# increases damage counter on rig by 1. Helper function accessed by other functions (eg data spike attack)
Asus.increase_damage()

# Constructs a string to return the damage and upgrade level of the rig
Asus.rig_condition()

# function to generate a random asset and place into rig inventory
Asus.generate_asset()

#Asset class has just basic setters and getters ,along with a string constructor

#Undefined behaviour - What gets blocked when hacker is exposed?
#Undefined behaviour - How is trace level reduce?
#Undefined behaviour - What is storage size of inventory and storage? Is it quantity of items or type of items?
#Undefined behaviour - How much is battle damage multiplied by when using upgrades?
