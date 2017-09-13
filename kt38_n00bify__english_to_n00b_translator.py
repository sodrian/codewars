"""Title: N00bify - English to n00b Translator
URL: https://www.codewars.com/kata/n00bify-english-to-n00b-translator
Description:

The internet is a very confounding place for some adults. Tom has just joined an online forum and is trying to fit in with all the teens and tweens. It seems like they're speaking in another language! Help Tom fit in by translating his well-formatted English into n00b language.

The following rules should be observed:

- "to" and "too" should be replaced by the number 2, even if they are only part of a word (E.g. today = 2day)
- Likewise, "for" and "fore" should be replaced by the number 4
- Any remaining double o's should be replaced with zeros (E.g. noob = n00b)
- "be", "are", "you", "please", "people", "really", "have", and "know" should be changed to "b", "r", "u", "plz", "ppl", "rly", "haz", and "no" respectively (even if they are only part of the word)
- When replacing words, always maintain case of the first letter unless another rule forces the word to all caps.
- The letter "s" should always be replaced by a "z", maintaining case
- "LOL" must be added to the beginning of any input string starting with a "w" or "W"
- "OMG" must be added to the beginning (after LOL, if applicable,) of a string 32 characters<sup>1</sup> or longer
- All evenly numbered words<sup>2</sup> must be in ALL CAPS (<b>Example:</b> ```Cake is very delicious.``` becomes ```Cake IZ very DELICIOUZ```)
- If the input string starts with "h" or "H", the entire output string should be in ALL CAPS
- Periods ( . ), commas ( , ), and apostrophes ( ' ) are to be removed
- <sup>3</sup>A question mark ( ? ) should have more question marks added to it, equal to the number of words<sup>2</sup> in the sentence (<b>Example:</b> ```Are you a foo?``` has 4 words, so it would be converted to ```r U a F00????```)
- <sup>3</sup>Similarly, exclamation points ( ! ) should be replaced by a series of alternating exclamation points and the number 1, equal to the number of words<sup>2</sup> in the sentence (<b>Example:</b> ```You are a foo!``` becomes ```u R a F00!1!1```)

<sup>1</sup> Characters should be counted <b>After:</b> any word conversions, adding additional words, and removing punctuation. <b>Excluding:</b> All punctuation and any 1's added after exclamation marks ( ! ). Character count <b>includes</b> spaces.

<sup>2</sup> For the sake of this kata, "words" are simply a space-delimited substring, regardless of its characters. Since the output may have a different number of words than the input, words should be counted based on the output string.

<b>Example:</b> ```whoa, you are my 123 <3``` becomes ```LOL WHOA u R my 123 <3``` = 7 words

<sup>3</sup>The incoming string will be punctuated properly, so punctuation does not need to be validated.
"""

import re
from string import maketrans

REPLACES = [
    ('too', '2'),
    ('to', '2'),
    ('fore', '4'),
    ('for', '4'),
    ('oo', '00'),
    ('be', 'b'),
    ('are', 'r'),
    ('you', 'u'),
    ('please', 'plz'),
    ('people', 'ppl'),
    ('really', 'rly'),
    ('have', 'haz'),
    ('know', 'no'),
    ('s', 'z')]
PUNCTS = ".,'"


def n00bify(text):
    orig_text = str(text)
    
    for k, v in REPLACES:
        text, numm = re.subn(k, v, text, count=10, flags=re.IGNORECASE)

    for p in PUNCTS:
        text = text.replace(p, '')
	
    if text[0].lower() == 'w':
        text = 'LOL ' + text
	
    if len(text.replace('!','')) >= 32:
        text = 'OMG ' + text
  	
    text = text.split()
    
    if text[0] == 'OMG' and text[1] == 'LOL':
        text[0], text[1] = text[1], text[0]
    
    text = ' '.join([i % 2 and word.upper() or word for i, word in enumerate(text)])
    
    if text[0].lower() == 'h':
        text = text.upper()
    
    indexes = sorted([i for i, let in enumerate(text) if let == '?'], reverse=True)
    for ind in indexes:
        text = text[:ind] + '?' * (len(text.split())) + text[ind+1:]
    
    indexes = sorted([i for i, let in enumerate(text) if let == '!'], reverse=True)
    for ind in indexes:
        text_len = len(text.split())
        excl_text = ''
        for i in range(text_len):
            excl_text += i % 2 and '1' or '!'
        text = text[:ind] + excl_text + text[ind+1:]
        
    return text