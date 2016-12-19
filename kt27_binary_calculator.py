import re
BIN_PTRN = r'([-]{0,1})0b(\d+)'

def calculate(n1, n2, o):
    add = lambda x, y: x + y
    subtract = lambda x, y: x - y
    multiply = lambda x, y: x * y 
    divide = lambda x, y: x / y
    f = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide}
    return ''.join(re.findall(BIN_PTRN, bin(f[o](int(n1, 2), int(n2, 2))))[0])