def switchFunc(version):
    with open(version, 'r') as file:
        filedata = file.read()
    if filedata == '1':
        filedata = filedata.replace('1', '0')
        print('UAV OFF')
    elif filedata == '0':
        filedata = filedata.replace('0', '1')
        print('UAV ON')
    with open(version, 'w') as file:
        file.write(filedata)


if __name__ == '__main__':
    switchFunc('drone_state.txt')
