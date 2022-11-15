#!/usr/bin/python
# -*- coding: utf-8 -*-

# File name: droneCRTL.py
# Author: Daniel Bosman
# Date created: 15/11/2022
# Date last modified: 15/11/2022
# Python version: 3.10.7

import droneOFF
import droneON
import random
import time
from datetime import datetime
import itertools as it

version_number = 1.0
kawaii_list = [
        " (⌐▨_▨)",
        " (⌐■_■)",
        " (ﾒ■_■)y-～"]

uav_status = 1
route = []
buildings = []
clouds = []

flag = False

print("──────────────────")
print("@ droneCTRL v"+str(version_number)+random.choice(kawaii_list))
print("$",datetime.now())
print("──────────────────")

while uav_status != 1:
        x_input = input("TYPE (X) TO CHECK UAV STATUS: ")
        print("──────────────────")

        if x_input == 'X':
                print("@ CHECKING UAV STATUS")
                time.sleep(3)
                if uav_status == 0:
                        print("! UAV NOT PRESENT")
                        print("──────────────────")
                        time.sleep(3)
                        y_input = input("TYPE (E) TO START UAV: ")
                        if y_input == "E":
                                print("──────────────────")
                                print("@ EXECUTING TASK")
                                time.sleep(3)
                                uav_status = 1
                                print("$ TASK EXECUTED SUCESSFULLY")
                if uav_status == 1:
                        time.sleep(3)
                        print("──────────────────")
                        print("! UAV PRESENT")
                        print("──────────────────")

z_input = input("TYPE (A) TO START SURVEY: ")
if z_input == "A":
        print("──────────────────")
        print("BATTERY_PERCENTAGE")
        print("──────────────────")
        for i in range(random.randrange(79, 100), 0, -3):
                print(str(i)+"%")
                time.sleep(1)
                if i < 35 and flag == False:
                        print("──────────────────")
                        print("LOW BATTERY")
                        print("──────────────────")
                        flag = True
                if i < 25:
                        print("──────────────────")
                        print("BATTERY TOO LOW; ENDING SURVEY")
                        print("──────────────────")
                        break