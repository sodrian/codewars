"""Title: Product of consecutive Fib numbers
URL: https://www.codewars.com/kata/product-of-consecutive-fib-numbers
Description:

The Fibonacci numbers are the numbers in the following integer sequence (Fn):
>0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such as 
>F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying 
>F(n) * F(n+1) = prod.

Your function productFib takes an integer (prod) and returns
an array: 
```
[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
```
depending on the language if F(n) * F(n+1) = prod.

If you don't find two consecutive F(m) verifying `F(m) * F(m+1) = prod`you will return
```
[F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
```
F(m) being the smallest one such as `F(m) * F(m+1) > prod`.

# Examples

```ruby
productFib(714) # should return [21, 34, true], 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return [34, 55, false], 
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
```
```crystal
productFib(714) # should return [21, 34, true], 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return [34, 55, false], 
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
```
```python
productFib(714) # should return [21, 34, true], 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return [34, 55, false], 
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
```
```clojure
productFib(714) # should return [21, 34, true], 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return [34, 55, false], 
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
```
```javascript
productFib(714) # should return [21, 34, true], 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return [34, 55, false], 
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
```
```php
productFib(714) # should return [21, 34, true], 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return [34, 55, false], 
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
```
```coffeescript
productFib(714) # should return [21, 34, true], 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return [34, 55, false], 
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
```
```csharp
productFib(714) # should return {21, 34, 1}, 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return {34, 55, 0}, 
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
```
```java
productFib(714) # should return {21, 34, 1}, 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return {34, 55, 0}, 
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
```
```cpp
productFib(714) # should return {21, 34, true}, 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return {34, 55, false}, 
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
```
```haskell
productFib 714 -- should return (21, 34, True)
               -- since F(8) = 21, F(9) = 34 and 714 = 21 * 34
productFib 800 -- should return (34, 55, False), 
               -- since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
```

**Note:** Not useful here but we can tell how to choose the number n up to which to go: we can use the "golden ratio" phi which is `(1 + sqrt(5))/2` knowing that F(n) is asymptotic to: `phi^n / sqrt(5)`. That gives a possible upper bound to n.

### References 

http://en.wikipedia.org/wiki/Fibonacci_number

http://oeis.org/A000045
"""

def productFib(prod):
    fib = [0, 1]
    while True:
        cur_fib = fib[-1] + fib[-2]
        next_fib = cur_fib + fib[-1]
        if cur_fib * next_fib == prod:
            return [cur_fib, next_fib, True]
        elif cur_fib * next_fib > prod:
            return [cur_fib, next_fib, False]
        fib.append(cur_fib)