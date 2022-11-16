def switchFunc(version):
    search_On = 'ON'
    search_OFF = 'OFF'
    try:
        with open(version, 'r') as file:
            for index, line in enumerate(file):
                if 'ON' in line:

