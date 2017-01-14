"""Title: Vowel Count
URL: https://www.codewars.com/kata/vowel-count
Description:

Return the number (count) of vowels in the given string. 

We will consider a, e, i, o, and u as vowels for this Kata.
"""

def getCount(inputStr):
    return len([ch for ch in inputStr.lower() if ch in 'aeiou'])