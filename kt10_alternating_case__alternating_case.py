def to_alternating_case(string):
    return ''.join([ch.upper() if ch.islower() else ch.lower() for ch in string])