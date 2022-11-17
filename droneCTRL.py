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
import time
import auth
import bat_dec
import bat_set
import x_pos_inc
import x_pos_set
import drone_state

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

z_input = input("TYPE (A) TO START SURVEY: ")
if z_input == "A":
    print("──────────────────")
    print("X_POS", "BAT")
    x_pos_set.x_pos_set()
    bat_set.bat_set()

    low_bat_flag = False

    while 1:
        with open('x_pos.txt') as f:
            x = f.readlines()
        with open('bat.txt') as f:
            y = f.readlines()
        if int(y[0]) < 25:
            print("! BATTERY BELOW 25; ENDING SURVEY")
            end_flag = True
            break
        elif int(y[0]) < 35 and low_bat_flag is False:
            print("! LOW BATTERY")
            low_bat_flag = True
        print(x[0], y[0])
        x_pos_inc.x_pos()
        bat_dec.bat_dec()
        time.sleep(1)

time.sleep(3)
print("@ EXECUTING TASK")
drone_state.switchFunc()
print("$ TASK EXECUTED SUCCESSFULLY")
