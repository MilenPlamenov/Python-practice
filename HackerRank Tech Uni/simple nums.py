# def is_prime(n):
#     if n == 2 or n == 3:
#         return True
#     if n < 2 or n % 2 == 0:
#         return False
#     if n < 9:
#         return True
#     if n % 3 == 0:
#         return False
#     r = int(n ** 0.5)
#     f = 5
#     while f <= r:
#         print('\t', f)
#         if n % f == 0:
#             return False
#         if n % (f + 2) == 0:
#             return False
#         f += 6
#     return True


import math


# def isprime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True


def primeSieve(sieveSize):

    # the Sieve of Eratosthenes algorithm.

    sieve = [True] * sieveSize

    sieve[0] = False  # zero and one are not prime numbers

    sieve[1] = False

    # create the sieve

    for i in range(2, int(math.sqrt(sieveSize)) + 1):

        pointer = i * 2

        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i

    primes = []

    for i in range(sieveSize):
        if sieve[i]:
            primes.append(i)

    return primes


print(primeSieve(1000000000)) # 1000000000000


# n = int(input())
#
# for _ in range(n):
#     num = int(input())
#
#     if not isprime(num):
#         print("NO")
#     else:
#         print("YES")
