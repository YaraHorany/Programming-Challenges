# Given an integer n, return the number of prime numbers that are strictly less than n.
"""
Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""

def countPrimes(n):
    if n <= 2:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False

    for p in range(2, n):
        if primes[p]:
            for i in range(2 * p, len(primes), p):
                if primes[i] == True:
                    primes[i] = False
            # primes[2 * p: n: p] = [False] * len(primes[2 * p: n: p])

    return sum(primes) # using sum() to count True values in primes list

print(countPrimes(10)) # expected: 4
print(countPrimes(0)) # expected: 0
print(countPrimes(0)) # expected: 0