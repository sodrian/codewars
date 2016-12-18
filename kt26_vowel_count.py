def getCount(inputStr):
    return len([ch for ch in inputStr.lower() if ch in 'aeiou'])