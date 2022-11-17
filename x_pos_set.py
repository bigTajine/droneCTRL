#!/usr/bin/python
# -*- coding: utf-8 -*-

# File name: x_pos_set.py
# Date created: 15/11/2022
# Date last modified: 16/11/2022
# Python version: 3.11.0

def x_pos_set():
    with open('x_pos.txt', 'w') as file:
        x_coordinates = 0
        # print(x)
        file.write(str(x_coordinates))


if __name__ == '__main__':
    x_pos_set()
