import sys
import os
from pathlib import Path
from utils import *

def main(code_path):
    # Loads the code and the array on the memory
    code, array = open_code(code_path)

    # Creates and opens the output file
    try:
        os.mkdir('out')
    except FileExistsError:
        pass
    output = open(Path('out/code.py'), 'w+')

    # Initializes the required functions, the array and the pointer to the output file
    with open('basic_functions.py', 'rt') as f:
        output.write(f.read())
    output.write(f'array = {array}\n')
    output.write(f'pointer = 0\n')

    # Initializes the identation variable
    identation = ''

    # Converts
    for character in code:
        match character:
            case '>':
                output.write(f'{identation}pointer = move_right_pointer(array, pointer)\n')
            case '<':
                output.write(f'{identation}pointer = move_left_pointer(array, pointer)\n')
            case '+':
                output.write(f'{identation}increase_pointer(array, pointer)\n')
            case '-':
                output.write(f'{identation}decrease_pointer(array, pointer)\n')
            case '.':
                output.write(f'{identation}print_pointer(array, pointer)\n')
            case ',':
                output.write(f'{identation}input_pointer(array, pointer)\n')
            case '[':
                identation = insert_loop_open(output, identation)
            case ']':
                identation = insert_loop_close(identation)
    
    # Closes the file
    output.close()


if __name__ == "__main__":
    # Check file existance
    try:
        if Path(sys.argv[1]).is_file():
            main(sys.argv[1])
            print('It\'s done! :)')
        else:
            print('The first argument must be the path to the .bf file. ')
            exit(1)
    except IndexError:
        print('You must specify the path to the .bf file. ')
        exit(1)
