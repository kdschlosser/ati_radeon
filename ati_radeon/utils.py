def get_string(data):
    try:
        unicode = unicode
    except NameError:
        unicode = bytes

    res = ''

    if isinstance(data, (str, unicode)):
        data = list(data)

        while data:
            char = data.pop(0)
            res += chr(char)

    else:
        i = 0
        while True:
            char = data[i]
            if isinstance(char, unicode):
                char = str(char, encoding='utf-8')

            if char in ('\x00', 0x00):
                break

            if isinstance(char, int):
                char = chr(char)

            res += char
            i += 1

    return res