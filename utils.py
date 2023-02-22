def open_code(code_path) -> str:
    """
    Opens a Brainf*ck code, defines the array size and returns the pure Brainf*ck code and the main array
    :param code_path: the .bf code's path
    :returns: the pure .bf code and the main array
    """
    code, array = [], []
    RECOGNIZEABLE_CHARACTERS = ['<', '>', '[', ']', '+', '-', '.', ',']
    with open(code_path, "r") as file:
        first_line = file.readline()
        if first_line[0] == "$":
            array_size = [x for x in first_line]
            array_size.pop(0)
            array_size = int(''.join(array_size))
            for i in range(0, array_size):
                array.append(0)
        else:
            for i in range(0, 30000):
                array.append(0)
        
        for line in file:
            clean_line = []
            for character in line:
                if character in RECOGNIZEABLE_CHARACTERS:
                    clean_line.append(character)
            clean_line = ''.join(clean_line)
            code.append(clean_line)
    
    code = ''.join(code)

    while '[]' in code:
        code = code.replace('[]', '')

    loops = 0
    for character in code:
        if character == '[':
            loops += 1
        if character == ']':
            loops -= 1
    if bool(loops):
        raise SyntaxError('there are some square brackets without a matching pair')

    return code, str(array)

