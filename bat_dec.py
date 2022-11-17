#!/usr/bin/python
# -*- coding: utf-8 -*-

# File name: bat_dec.txt
# Date created: 15/11/2022
# Date last modified: 16/11/2022
# Python version: 3.11.0

import random


def bat_dec():
    with open('bat.txt') as f:
        x = f.readlines()
        # print(x[0])

        y = int(x[0]) - random.randrange(1, 3)
        # print(y)

    with open('bat.txt', 'w') as f:
        f.write(str(y))

if __name__ == '__main__':
    bat_dec()