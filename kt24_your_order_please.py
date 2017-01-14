"""Title: Your order,  please
URL: https://www.codewars.com/kata/your-order-please
Description:

Your task is to sort a given string.
Each word in the String will contain a single number. 
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String.
The words in the input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"
"""

import re
PTRN = r'[a-zA-Z]*(\d+)[a-zA-Z]*'


def order(sentence):
    ret = list()
    for el in sentence.split(' '):
        if el:
            d = re.findall(PTRN, el)[0]
            ret.append([d, el])
    ret = sorted(ret, key=lambda el: el[0])
    return ' '.join([el[1] for el in ret])