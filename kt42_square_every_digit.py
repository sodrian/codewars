"""Title: Square Every Digit
URL: https://www.codewars.com/kata/square-every-digit
Description:

Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 9<sup>2</sup> is 81 and 1<sup>2</sup> is 1.

**Note:** The function accepts an integer and returns an integer
"""

def square_digits(num):
    num = [int(str(num)[i]) for i in range(len(str(num)))]
    return int(''.join([str(n ** 2) for n in num]))