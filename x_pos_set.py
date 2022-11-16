#!/usr/bin/python
# -*- coding: utf-8 -*-

# File name: x_pos_set.py
# Date created: 15/11/2022
# Date last modified: 16/11/2022
# Python version: 3.11.0

def func1():
    with open('x_pos.txt', 'w') as f:
        x = 0
        # print(x)
        f.write(str(x))


if __name__ == '__main__':
    func1()
