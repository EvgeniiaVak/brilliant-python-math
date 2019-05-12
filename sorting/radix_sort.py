import random
import math

def sort(a, radix):
    if len(a) < 2:
        return a

    m = int(math.log(max(a), radix)) + 1
    for i in range(m):
        a = part_sort(a, i, radix)
    return a

def part_sort(a, pos, radix):
    counters = [0] * radix
    result = [None]*len(a)

    for i in a:
        counters[(i // (10 ** pos) ) % radix] += 1

    for i in range(1, radix):
        counters[i] += counters[i-1]

    for i in range(-1, -(len(a) + 1), -1):
        value = a[i]
        rem = (value // (10 ** pos) ) % radix
        counters[rem] -= 1
        result[counters[rem]] = value

    return result

def test_part():
    for _ in range(10):
        a = random.sample(range(10, 100), random.randrange(5, 10))
        print(f'\ntesting\n{a}')
        actual = part_sort(a, 0, 10)
        print(actual)

def test():
    for _ in range(10):
        a = random.sample(range(10, 20), random.randrange(5, 6))
        print(f'\ntesting {a}')
        expected = sorted(a)
        actual = sort(a, 10)
        assert expected == actual
        print('success')