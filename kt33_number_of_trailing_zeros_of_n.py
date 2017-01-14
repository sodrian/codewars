"""Title: Number of trailing zeros of N!
URL: https://www.codewars.com/kata/number-of-trailing-zeros-of-n
Description:

Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 \* 2 \* 3 \* 4 ... N


```
zeros(12) = 2 # 1 * 2 * 3 .. 12 = 479001600 
that has 2 trailing zeros 4790016(00)
```


Be careful 1000! has length of 2568 digital numbers.
"""

def zeros(n):
    ret = 0
    i = 5
    
    while n / i >= 1:
        ret += n // i
        i *= 5
    
    return ret