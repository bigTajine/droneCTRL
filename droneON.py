def switchFunc(version):
    with open(version, 'r') as file:
      filedata = file.read()
    if filedata == 'ON':
      filedata = filedata.replace('ON', 'OFF')
    elif filedata == 'OFF':
      filedata = filedata.replace('OFF', 'ON')
    with open(version, 'w') as file:
      file.write(filedata)

if __name__ == '__main__':
  switchFunc('drone.txt')