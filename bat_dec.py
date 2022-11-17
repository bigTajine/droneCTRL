#!/usr/bin/python
# -*- coding: utf-8 -*-

# File name: bat_dec.txt
# Date created: 15/11/2022
# Date last modified: 16/11/2022
# Python version: 3.11.0

import random


def bat_dec():
    with open('bat.txt') as file:
        file_read = file.readlines()
        # print(x[0])

        dec_bat = int(file_read[0]) - random.randrange(1, 3)
        # print(y)

    with open('bat.txt', 'w') as file:
        file.write(str(dec_bat))


if __name__ == '__main__':
    bat_dec()
