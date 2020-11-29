"""
Leonardo loves primes and created  queries where each query takes the form of an integer, .
For each , count the maximum number of distinct prime factors of any number in the inclusive range .

Note: Recall that a prime number is only divisible by  and itself, and  is not a prime number.

Example

The maximum number of distinct prime factors for values less than or equal to  is . One value with  distinct prime factors is . Another is .

Function Description

Complete the primeCount function in the editor below.

primeCount has the following parameters:

int n: the inclusive limit of the range to check
Returns

int: the maximum number of distinct prime factors of any number in the inclusive range .
Input Format

The first line contains an integer, , the number of queries.
Each of the next  lines contains a single integer, .
"""

from functools import reduce


def prime_count(n):

    if n == 1:
        return 0
    if n == 2:
        return 1

    primes = [2]

    check_factor_is_prime = lambda factor: all(factor % x for x in primes)
    get_primes_multipliation = lambda: reduce(lambda x, y: x * y, primes)

    for factor in range(3, n + 1, 2):
        if check_factor_is_prime(factor):
            primes.append(factor)
        if get_primes_multipliation() >= n:
            break

    if get_primes_multipliation() == n:
        return len(primes)
    return len(primes) - 1


if __name__ == '__main__':
    print('Answer: ', prime_count(100))