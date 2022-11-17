#!/usr/bin/python
# -*- coding: utf-8 -*-

# File name: drone_state.py
# Date created: 15/11/2022
# Date last modified: 16/11/2022
# Python version: 3.11.0

from datetime import datetime
import random
import time


def switchFunc():
    kawaii_list = [
        "(▼O▼ﾒ)",
        "(╭ರ_•́)",
        "(▼ω▼o)y-~~~"]

    print("──────────────────")
    print("@ drone_state", "version 1.0", random.choice(kawaii_list))
    print("$", datetime.now())
    print("──────────────────")
    time.sleep(3)
    with open("drone_state.txt", 'r') as file:
        filedata = file.read()
    if filedata == '1':
        filedata = filedata.replace('1', '0')
        print('! UAV OFF')
    elif filedata == '0':
        filedata = filedata.replace('0', '1')
        print('! UAV ON')
    with open("drone_state.txt", 'w') as file:
        file.write(filedata)
    print("──────────────────")


if __name__ == '__main__':
    switchFunc()
