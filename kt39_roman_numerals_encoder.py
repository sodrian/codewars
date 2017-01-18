"""Title: Roman Numerals Encoder
URL: https://www.codewars.com/kata/roman-numerals-encoder
Description:

Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Example:
```javascript
solution(1000); // should return 'M'
```
```coffeescript
solution(1000) # should return 'M'
```
```ruby
solution(1000) # should return 'M'
```
```python
solution(1000) # should return 'M'
```
```haskell
solution 1000 -- should return "M"
```
```java
conversion.solution(1000); //should return "M"
```
```typescript
solution(1000); // should return 'M'
```

Help:
```
Symbol	Value
I	      1
V	      5
X	      10
L	      50
C	      100
D	      500
M	      1,000
```

Remember that there can't be more than 3 identical symbols in a row.


More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals
"""

D = [
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400), 
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1)]

def solution(n):
    ret = ''
    i = 0
    
    while True:
        res, n = divmod(n, D[i][1])
        if not res and not n:
            break
        elif res:
            ret += D[i][0] * res
        elif not res:
            i += 1
    
    return ret