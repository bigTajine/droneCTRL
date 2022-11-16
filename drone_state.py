#!/usr/bin/python
# -*- coding: utf-8 -*-

# File name: drone_state.py
# Date created: 15/11/2022
# Date last modified: 16/11/2022
# Python version: 3.11.0

def switchFunc(version):
    with open(version, 'r') as file:
        filedata = file.read()
    if filedata == '1':
        filedata = filedata.replace('1', '0')
        print('UAV OFF')
    elif filedata == '0':
        filedata = filedata.replace('0', '1')
        print('UAV ON')
    with open(version, 'w') as file:
        file.write(filedata)


    return switchFunc('drone_state.txt')
