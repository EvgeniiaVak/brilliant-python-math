def merge(l, r):
    result = []
    while l and r:
        if l[0] > r[0]:
            result.append(r.pop(0))
        else:
            result.append(l.pop(0))
    result.extend(l)
    result.extend(r)
    return result

def sort(a):
    print(f'sorting: {a}...')
    halfway = len(a) // 2
    if len(a) == 1:
        return a
    else:
        return merge(sort(a[:halfway]), sort(a[halfway:]))


def test_reverse():
    assert [1,2,3,4] == sort([4,3,2,1])

def test_negative():
    assert [-15, -10, 0, 12, 43] == sort([43, 0, -15, -10, 12])