#!/usr/bin/python
# -*- coding: utf-8 -*-

# File name: droneCRTL.py
# Date created: 15/11/2022
# Date last modified: 16/11/2022
# Python version: 3.11.0

'''
Import statements
'''

from datetime import datetime
import random
import time

import x_pos_set
import bat_set
import x_pos_inc
import bat_dec
from version_control import *
from droneON import *
'''
Initialization
'''

version_number = 1.0
kawaii_list = [
    " (⌐▨_▨)",
    " (⌐■_■)",
    " (ﾒ■_■)y-～"]

uav_status = 1
route = []
buildings = []
clouds = []

'''
Start of the Drone Controller
'''

print("──────────────────")
print("@ droneCTRL " + Information('version_control.txt') + random.choice(kawaii_list))
print("$", datetime.now())
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
    print("X_POS","BAT")
    x_pos_set.func1()
    bat_set.func1()

    low_bat_flag = False

    while 1:
        with open('x_pos.txt') as f:
            x = f.readlines()
        with open('bat.txt') as f:
            y = f.readlines()
        if int(y[0]) < 35 and low_bat_flag == False:
            print("LOW BATTERY")
            low_bat_flag = True
        if int(y[0]) < 25:
            print("BATTERY BELOW 25; ENDING SURVEY")
            end_flag = True
            break
        print(x[0],y[0])
        x_pos_inc.func1()
        bat_dec.func1()
        time.sleep(1)