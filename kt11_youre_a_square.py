import math

def is_square(n):
    try:
        r = math.sqrt(n)
        return r == int(r)
    except ValueError:
        return False