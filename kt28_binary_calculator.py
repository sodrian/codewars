"""Title: Binary Calculator
URL: https://www.codewars.com/kata/binary-calculator
Description:

In this kata you need to write a function that will receive two strings (```n1``` and ```n2```), each representing an integer as a binary number. A third parameter will be provided (```o```) as a string representing one of the following operators: add, subtract, multiply.

Your task is to write the calculate function so that it will perform the arithmetic and the result returned should be a string representing the binary result.

Examples:
```
1 + 1 === 10
10 + 10 === 100
```

Negative binary numbers are usually preceded by several 1's. For this kata, negative numbers can be represented with the negative symbol at the beginning of the string.

Examples of negatives:
```
1 - 10 === -1
10 - 100 === -10
```
"""

import re
from operator import add, sub, mul
BIN_PTRN = r'([-]{0,1})0b(\d+)'

def calculate(n1, n2, o):
    f = {
        'add': add,
        'subtract': sub,
        'multiply': mul}
    return ''.join(re.findall(BIN_PTRN, bin(f[o](int(n1, 2), int(n2, 2))))[0])