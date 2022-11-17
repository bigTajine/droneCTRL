#!/usr/bin/python
# -*- coding: utf-8 -*-

# File name: x_pos_inc.py
# Date created: 15/11/2022
# Date last modified: 16/11/2022
# Python version: 3.11.0

import random


def x_pos():
    with open('x_pos.txt') as file:
        x_coordinates = file.readlines()
        # print(x[0])

        position_increment = int(x_coordinates[0]) + random.randrange(10, 15)
        # print(y)

    with open('x_pos.txt', 'w') as f:
        f.write(str(position_increment))


if __name__ == '__main__':
    x_pos()
