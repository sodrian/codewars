"""Title: Next bigger number with the same digits
URL: https://www.codewars.com/kata/next-bigger-number-with-the-same-digits
Description:

You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:
```javascript
nextBigger(12)==21
nextBigger(513)==531
nextBigger(2017)==2071
```
```python
next_bigger(12)==21
next_bigger(513)==531
next_bigger(2017)==2071
```
```ruby
next_bigger(12)==21
next_bigger(513)==531
next_bigger(2017)==2071
```
```csharp
Kata.NextBiggerNumber(12)==21
Kata.NextBiggerNumber(513)==531
Kata.NextBiggerNumber(2017)==2071
```
```java
Kata.nextBiggerNumber(12)==21
Kata.nextBiggerNumber(513)==531
Kata.nextBiggerNumber(2017)==2071
```
If no bigger number can be composed using those digits, return -1:
```javascript
nextBigger(9)==-1
nextBigger(111)==-1
nextBigger(531)==-1
```
```python
next_bigger(9)==-1
next_bigger(111)==-1
next_bigger(531)==-1
```
```ruby
next_bigger(9)==-1
next_bigger(111)==-1
next_bigger(531)==-1
```
```csharp
Kata.NextBiggerNumber(9)==-1
Kata.NextBiggerNumber(111)==-1
Kata.NextBiggerNumber(531)==-1
```
```java
Kata.nextBiggerNumber(9)==-1
Kata.nextBiggerNumber(111)==-1
Kata.nextBiggerNumber(531)==-1
```
"""

from itertools import permutations

def sub_perm(iter_n):
    for el in permutations(''.join(sorted(iter_n))):
        el = ''.join(el)
        if el > iter_n:
            return int(el)
    else:
        return -1

def next_bigger(n):
    n = str(n)
    if len(n) == 1:
        return -1
    elif len(n) == 2:
        return sub_perm(n)
    elif len(n) > 2:
        for i in range(2, len(n)+1):
            iter_n = n[-i:]
            el = sub_perm(iter_n)
            if el > 0:
                return int('{0}{1}'.format(n[:-i], el))
    return -1