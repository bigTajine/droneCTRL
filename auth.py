# !/usr/bin/python
# -*- coding: utf-8 -*-

# File name: auth.py
# Date created: 15/11/2022
# Date last modified: 16/11/2022
# Python version: 3.11.0

def func1():
    user_flag = False

    while not user_flag:

        username = 'KStol1'
        password = 'KStol1'

        userInput = input("$ USERNAME: ")

        if userInput == username:
            a = input("# PASSWORD: ")
            if a == password:
                user_flag = True
                print("──────────────────")
                print("% WELCOME " + username + "!")
                print("──────────────────")
            else:
                print("──────────────────")
                print("^ WRONG PASSWORD")
                print("──────────────────")
        else:
            print("──────────────────")
            print("^ WRONG USERNAME")
            print("──────────────────")


if __name__ == '__main__':
    func1()
