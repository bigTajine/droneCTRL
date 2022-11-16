import random

def func1():

    with open('x_pos.txt', 'w') as f:
        x = 0
        # print(x)
        f.write(str(x))

if __name__ == '__main__':
    func1()