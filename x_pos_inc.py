import random


def func1():
    with open('x_pos.txt') as f:
        x = f.readlines()
        # print(x[0])

        y = int(x[0]) + random.randrange(10, 15)
        # print(y)

    with open('x_pos.txt', 'w') as f:
        f.write(str(y))

if __name__ == '__main__':
    func1()