"""Title: Simple Pig Latin
URL: https://www.codewars.com/kata/simple-pig-latin
Description:

Move the first letter of each word to the end of it, then add 'ay' to the end of the word.

```javascript
pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
```
```ruby
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
```
```python
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
```
```csharp
Kata.PigIt("Pig latin is cool"); // igPay atinlay siay oolcay
```
"""

import re
WORD_PTRN = r'^[\w]+$'

def pig_it(text):
    return ' '.join(['{0}{1}{2}'.format(word[1:], word[0], 'ay') if re.match(WORD_PTRN, word) else word for word in text.split()])