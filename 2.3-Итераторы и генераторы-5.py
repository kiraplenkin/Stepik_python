import itertools


def primes():
    a = 1
    while True:
        a += 1
        if all(a % i for i in range(2, a)):
            yield a

print(list(itertools.takewhile(lambda x: x <= 31, primes())))
