import random

def sort_with_array(a):
    if len(a) < 2:
        return a

    c = [None] * (max(a) + 1)
    for i in range(len(a)):
        if c[a[i]] is not None:
            c[a[i]] += 1
        else:
            c[a[i]] = 1

    result = [None] * len(a)

    index = 0
    for i in range(len(c)):
        if c[i] is not None:
            while c[i] > 0:
                result[index] = i
                index += 1
                c[i] -= 1

    return result

def sort_with_dict(a):
    if len(a) < 2:
        return a

    counters = {}
    max_value = a[0]
    min_value = a[0]

    for i in a:
        counters[i] = counters.get(i, 0) + 1
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i

    result = [None] * len(a)

    index = 0
    for i in range(min_value, max_value + 1):
        n = counters.get(i, None)
        if n is not None:
            while n > 0:
                result[index] = i
                index += 1
                n -= 1

    return result


def test_sort_with_array():
    for _ in range(10):
        a = random.sample(range(0, 10000), random.randrange(0, 10000))
        print(f'\ntesting {a}')
        expected = sorted(a)
        actual = sort_with_array(a)
        assert expected == actual
        print('success')

def test_sort_with_dict():
    for _ in range(10):
        a = random.sample(range(-10000, 10000), random.randrange(0, 10000))
        print(f'\ntesting {a}')
        expected = sorted(a)
        actual = sort_with_dict(a)
        assert expected == actual
        print('success')