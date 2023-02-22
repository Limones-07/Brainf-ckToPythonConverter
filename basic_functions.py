class NotCharException(Exception):
    def __init__(self, str, *args):
        super().__init__(*args)
        self.str = str
    
    def __str__(self):
        return f'\"{self.str}\" is not a character'


class NotASCIIException(Exception):
    def __init__(self, str, *args):
        super().__init__(*args)
        self.str = str

    def __str__(self):
        return f'\"{self.str}\" is not on ASCII table'
    

def increase_pointer(array: list, pointer: int):
    if pointer == len(array)-1:
        pointer = 0
    else:
        pointer += 1


def decrease_pointer(array: list, pointer: int):
    if pointer == 0:
        pointer = len(array)-1
    else:
        pointer -= 1

def add_pointer(array: list, pointer: int):
    if array[pointer] == 255:
        array[pointer] = 0
    else:
        array[pointer] += 1

def subtract_pointer(array: list, pointer: int):
    if array[pointer] == 0:
        array[pointer] = 255
    else:
        array[pointer] -= 1


def print_pointer(array: list, pointer: int):
    print(chr(array[pointer]))


def input_pointer(array: list, pointer: int):
    input_txt = str(input()).strip()
    if len(input_txt) == 1:
        if ord(input_txt) > 255:
            raise NotASCIIException(input_txt)
        array[pointer] = ord(input_txt)
    else:
        raise NotCharException(input_txt)

