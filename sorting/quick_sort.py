import random


def sort(a, l = 0, r = -1):
    if r == -1:
        r = len(a)
    if not a or len(a) == 1 or r - l <= 1:
        return

    pivot = l

    for i in range(l + 1, r):
        if a[i] <= a[l]:
            pivot += 1
            a[pivot], a[i] = a[i], a[pivot]

    a[pivot], a[l] = a[l], a[pivot]

    sort(a, l, pivot)
    sort(a, pivot + 1, r)


def test():
    for _ in range(10):
        a = random.sample(range(-10000, 10000), random.randrange(0, 10000))
        print(f'\ntesting {a}')
        expected = sorted(a)
        sort(a)
        assert expected == a
        print('success')