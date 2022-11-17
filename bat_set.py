#!/usr/bin/python
# -*- coding: utf-8 -*-

# File name: bat_set.py
# Date created: 15/11/2022
# Date last modified: 16/11/2022
# Python version: 3.11.0

import random


def bat_set():
    with open('bat.txt', 'w') as file:
        battery_set = random.randrange(80, 100)
        # print(x)
        file.write(str(battery_set))


if __name__ == '__main__':
    bat_set()
