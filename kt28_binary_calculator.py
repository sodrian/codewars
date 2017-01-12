import re
from operator import add, sub, mul
BIN_PTRN = r'([-]{0,1})0b(\d+)'

def calculate(n1, n2, o):
    f = {
        'add': add,
        'subtract': sub,
        'multiply': mul}
    return ''.join(re.findall(BIN_PTRN, bin(f[o](int(n1, 2), int(n2, 2))))[0])