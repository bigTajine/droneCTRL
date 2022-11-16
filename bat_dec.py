import random


def func1():
    with open('bat.txt') as f:
        x = f.readlines()
        # print(x[0])

        y = int(x[0]) - random.randrange(1, 3)
        # print(y)

    with open('bat.txt', 'w') as f:
        f.write(str(y))

if __name__ == '__main__':
    func1()