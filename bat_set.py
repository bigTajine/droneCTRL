#!/usr/bin/python
# -*- coding: utf-8 -*-

# File name: bat_set.py
# Date created: 15/11/2022
# Date last modified: 16/11/2022
# Python version: 3.11.0

import random

def func1():
    with open('bat.txt', 'w') as f:
        x = random.randrange(80, 100)
        # print(x)
        f.write(str(x))

if __name__ == '__main__':
    func1()