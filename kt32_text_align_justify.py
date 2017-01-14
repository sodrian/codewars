"""Title: Text align justify
URL: https://www.codewars.com/kata/text-align-justify
Description:

Your task in this Kata is to emulate text justification in monospace font. You will be given a single-lined text and the expected justification width. The longest word will never be greater than this width.

Here are the rules:

  * Use spaces to fill in the gaps between words.
  * Each line should contain as many words as possible.
  * Use '\n' to separate lines.
  * Gap between words can't differ by more than one space.
  * Lines should end with a word not a space.
  * '\n' is not included in the length of a line.
  * Large gaps go first, then smaller ones: 'Lorem---ipsum---dolor--sit--amet' (3, 3, 2, 2 spaces).
  * Last line should not be justified, use only one space between words.
  * Last line should not contain '\n'
  * Strings with one word do not need gaps ('somelongword\n').

Example with width=30:

```
Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor.
```

Also you can always take a look at how justification works in your text editor or directly in HTML (css: text-align: justify).

Have fun :)
"""

def line_justified(words, width):
    n_of_words = len(words)
    n_of_spaces = n_of_words and n_of_words - 1 or 0
    total_space = width - len(''.join(words))
    add_space = total_space - n_of_spaces
    
    spaces = [' '] * n_of_spaces
    if add_space and n_of_spaces:
    	for i in range(add_space):
            el = i % n_of_spaces
            spaces[el] += ' '
    
    ret = ''
    for i, word in enumerate(words):
        ret += word
        if i < len(spaces):
            ret += spaces[i]
    
    return ret
    

def justify(text, width):
    ret = []
    cur_line = []
    
    for word in text.split():
        cur_line_len = len(' '.join(cur_line))
        if cur_line_len + 1 + len(word) <= width:
            cur_line.append(word)
        else:
            ret.append(line_justified(cur_line, width))
            cur_line = [word, ]
    
    # last line must not be justified
    if line_justified(cur_line, width) != ret[-1]:
        ret.append(' '.join(cur_line))
    
    return '\n'.join(ret)