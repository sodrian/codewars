"""Title: Fake Binary
URL: https://www.codewars.com/kata/fake-binary
Description:

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
"""

def fake_bin(x):
    return ''.join([str(int(d) // 5) for d in x]) 