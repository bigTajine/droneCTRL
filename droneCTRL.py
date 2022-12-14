#!/usr/bin/python
# -*- coding: utf-8 -*-

# File name: droneCRTL.py
# Date created: 15/11/2022
# Date last modified: 16/11/2022
# Python version: 3.11.0

'''
Import statements
'''

import datetime
import random

import auth
import drone_state
from Drone import *

'''
Initialization
'''

kawaii_list = [
    "(⌐▨_▨)",
    "(⌐■_■)",
    "(ﾒ■_■)y-～"]

auth_bypass = False  # Set to true to skip authentication during development.
uav_flag = False
uav_status = int(open("drone_state.txt", "r").read())
version_control = open("version_control.txt", "r").read()

route = []
buildings = []
clouds = []

'''
Start of the Drone Controller
'''

print("──────────────────")
print("@ droneCTRL", version_control, random.choice(kawaii_list))
print("$", datetime.datetime.now())
print("──────────────────")

if not auth_bypass:
    auth.func1()

while uav_status != 1:
    x_input = input("TYPE (X) TO CHECK UAV STATUS: ")
    print("──────────────────")

    if x_input == 'X':
        while not uav_flag:
            print("@ CHECKING UAV STATUS")
            uav_status = int(open("drone_state.txt", "r").read())
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
                    drone_state.switchFunc()
                    print("$ TASK EXECUTED SUCESSFULLY")
            if uav_status == 1:
                time.sleep(3)
                print("! UAV PRESENT")
                print("──────────────────")
                uav_flag = True

time.sleep(3)
print("% ROUTE IMPORTED")
print("──────────────────")
z_input = input("TYPE (A) TO START SURVEY: ")
if z_input == "A":
    print("──────────────────")
    exec(open("Drone.py").read())

time.sleep(3)
print("@ EXECUTING TASK")
drone_state.switchFunc()
print("$ TASK EXECUTED SUCCESSFULLY")
