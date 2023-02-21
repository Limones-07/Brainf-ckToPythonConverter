import sys
import os.path

RECOGNIZEABLE_CHARACTERS = ['<', '>', '[', ']', '+', '-', '.', ',']

def open_code(code_path) -> str:
    """
    Opens a Brainf*ck code, defines the array size and returns the pure Brainf*ck code and the main array
    :param code_path: the .bf code's path
    :returns: the pure .bf code and the main array
    """
    file = open(code_path, "r")
    code, array = [], []

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
    return ''.join(code), array

def main(code_path):
    code_path = 'code.bf'
    code, array = open_code(code_path)
    print(code)
    print(array)

if __name__ == "__main__":
    # Check file existance
    if os.path.isfile(sys.argv[1]):
        main(sys.argv[1])
    else:
        print('The first argument must be the path to the .bf file. ')
        exit(1)
