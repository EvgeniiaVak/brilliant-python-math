import random


def sort(a):
    if len(a) < 2:
        return a
    # count how many times a number occurs
    counters = []
    for i in a:
        if len(counters) < i + 1:
            counters.extend([0] * ((i + 1) - len(counters)))
        counters[i] += 1

    # count how far each number is in the array
    for i in range(1, len(counters)):
        counters[i] = counters[i] + counters[i - 1]

    #fill in the result
    result = [None] * len(a)
    for i in a:
        counters[i] -= 1
        result[counters[i]] = i

    return result

def test_sort():
    for _ in range(10):
        a = random.sample(range(0, 10000), random.randrange(0, 10000))
        print(f'\ntesting {a}')
        expected = sorted(a)
        actual = sort(a)
        assert expected == actual
        print('success')