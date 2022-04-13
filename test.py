from math import sqrt
from time import perf_counter


def divisor_generator(n):
    ts = perf_counter()
    large_divisors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i ** 2 != n:
                large_divisors.append(int(n / i))
    for divisor in reversed(large_divisors):
        yield divisor
    tf  = perf_counter()
    print(tf - ts)


print(*list(divisor_generator(int(input()))))
