def Information(version):
    version_control = ''
    try:
        with open(version, 'r') as file:
            for index, line in enumerate(file):
                if 'version' in line:
                    version_control = line
                    break
    except Exception:
        version_control = 'version 1.0'

    return version_control


print(Information('version_control.txt'))
