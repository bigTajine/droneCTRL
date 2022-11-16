import random

def func1():
    with open('bat.txt', 'w') as f:
        x = random.randrange(80, 100)
        # print(x)
        f.write(str(x))

if __name__ == '__main__':
    func1()