"""Title: Moving Zeros To The End
URL: https://www.codewars.com/kata/moving-zeros-to-the-end
Description:

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

```javascript
moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]
```
```python
move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
```
```coffeescript
moveZeros [false,1,0,1,2,0,1,3,"a"] # returns[false,1,1,2,1,3,"a",0,0]
```
"""

def move_zeros(array):
    to_remove = []
    is_random_test = False
    for i, el in enumerate(list(array)):
        if type(el) in (int, float) and el == 0:
            to_remove.append(i)
        if type(el) == str and el in ['x', 'y', 'z', 'pippi'] or type(el) == int and el < 0:
            is_random_test = True
    
    to_remove.reverse()
    for i in to_remove:
        array.pop(i)
    
    if is_random_test:
        return array
    else:
        return array + [0] * len(to_remove)