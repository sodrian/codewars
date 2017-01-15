"""Title: ASCII hex converter
URL: https://www.codewars.com/kata/ascii-hex-converter
Description:

Write a module Converter that can take ASCII text and convert it to
hexadecimal. The class should also be able to take hexadecimal and
convert it to ASCII text.

Example

```ruby
Converter.to_hex("Look mom, no hands")
=> "4c6f6f6b206d6f6d2c206e6f2068616e6473"

Converter.to_ascii("4c6f6f6b206d6f6d2c206e6f2068616e6473")
=> "Look mom, no hands"
```
```python
Converter.to_hex("Look mom, no hands")
=> "4c6f6f6b206d6f6d2c206e6f2068616e6473"

Converter.to_ascii("4c6f6f6b206d6f6d2c206e6f2068616e6473")
=> "Look mom, no hands"
```
```javascript
Converter.toHex("Look mom, no hands")
=> "4c6f6f6b206d6f6d2c206e6f2068616e6473"

Converter.toAscii("4c6f6f6b206d6f6d2c206e6f2068616e6473")
=> "Look mom, no hands"
```
"""

class Converter():
    @staticmethod
    def to_ascii(h):
        return ''.join([chr(int(h[i] + h[i+1], 16)) for i in range(len(h))[::2]])
    @staticmethod
    def to_hex(s):
        return ''.join(['{0:X}'.format(ord(l)).lower() for l in s])