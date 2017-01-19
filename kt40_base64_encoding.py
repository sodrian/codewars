"""Title: Base64 Encoding
URL: https://www.codewars.com/kata/base64-encoding
Description:

Extend the String object (JS) or create a function (Python) that converts the value of the String **to and from Base64** using the ASCII character set.

**Usage:**
```javascript
// should return 'dGhpcyBpcyBhIHN0cmluZyEh'
'this is a string!!'.toBase64(); 

// should return 'this is a string!!'
'dGhpcyBpcyBhIHN0cmluZyEh'.fromBase64(); 
```
```python
# should return 'dGhpcyBpcyBhIHN0cmluZyEh'
to_base_64('this is a string!!')

# should return 'this is a string!!'
from_base_64('dGhpcyBpcyBhIHN0cmluZyEh')
```

You can learn more about Base64 encoding and decoding <a href="http://en.wikipedia.org/wiki/Base64">here</a>.
"""

import base64

def to_base_64(string):
    return base64.b64encode(string).rstrip('=')
    
def from_base_64(string):
    return base64.b64decode(string + '=' * (4 - len(string) % 4))