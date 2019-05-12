import math
import random

def gcd(a, b):
    # finding a gcd of two numbers a and b is like finding a largest
    # square copies of which can be used to fully cover the rectangle axb

    if a < b:
        a, b = b, a

    if a == b:
        return a

    return gcd(a - b, b)

def test():
    for i in range(10):
        l, r = random.randrange(1, 1000), random.randrange(1, 1000)
        assert math.gcd(l, r) == gcd(l, r)