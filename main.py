import sys
import os
import os.path
from functions import *

def main(code_path):
    # Loads the code and the array on the memory
    code, array = open_code(code_path)
    # print(code)
    # print(array)
    
    # Create and opens the output file
    try:
        os.mkdir('out')
    except FileExistsError:
        pass
    os.chdir('out')
    output = open('code.py', 'w+')

    output.close()


if __name__ == "__main__":
    # Check file existance
    try:
        if os.path.isfile(sys.argv[1]):
            main(sys.argv[1])
        else:
            print('The first argument must be the path to the .bf file. ')
            exit(1)
    except IndexError as e:
        print('You must provide the .bf file\'s path on the first argument. ')
        exit(1)
