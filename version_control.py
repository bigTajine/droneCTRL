#!/usr/bin/python
# -*- coding: utf-8 -*-

# File name: version_control.py
# Date created: 15/11/2022
# Date last modified: 16/11/2022
# Python version: 3.11.0

def information(version):
    version_control = ''
    try:
        with open(version, 'r') as file:
            for index, line in enumerate(file):
                if 'version' in line:
                    version_control = line
                    break
    except Exception:
        version_control = 'version 1.0'

    return version_control


print(information('version_control.txt'))
