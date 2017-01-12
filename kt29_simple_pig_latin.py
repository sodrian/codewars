import re
WORD_PTRN = r'^[\w]+$'

def pig_it(text):
    return ' '.join(['{0}{1}{2}'.format(word[1:], word[0], 'ay') if re.match(WORD_PTRN, word) else word for word in text.split()])