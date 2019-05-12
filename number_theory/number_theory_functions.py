primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199)


def prime_factors_dict(number):
    """:returns a dictionary with prime factors of the input number and their powers"""
    result = {}
    if number == 0:
        return result
    for p in primes:
        while number % p == 0:
            result[p]= result.get(p, 0) + 1
            number /= p
        if number == 0:
            break

    #TODO: find more primes if number is still not 0

    return result

def prime_factors_list(number):
    """:returns a list with prime factors of the input number"""
    result = []
    if number == 0:
        return result
    for p in primes:
        while number % p == 0:
            result.append(p)
            number /= p
        if number == 0:
            break

    #TODO: find more primes if number is still not 0

    return result

def lcm(a,b):

    if a == 0 or b == 0:
        return 0

    a_primes = prime_factors_dict(a)
    b_primes = prime_factors_dict(b)

    result=1

    for f, p in a_primes.items():
        result *= f**max(p, b_primes.pop(f, 0))

    for f, p in b_primes.items():
        result *= f**p

    return result

def number_from(factors):
    if factors is None or not factors:
        return 0
    result=1
    for i in factors:
        result *= i
    return result
