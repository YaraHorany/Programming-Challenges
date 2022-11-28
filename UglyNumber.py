# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

def isUgly(n):
	if n == 0:
		return False
	while n % 5 == 0:
		n /= 5
	while n % 3 == 0:
		n /= 3
	while n % 2 == 0:
		n /= 2
	return n == 1


print(isUgly(6)) # expected output: True, 6 = 2 × 3
print(isUgly(1)) # expected output: True, 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
print(isUgly(14)) # expected output: False, 14 not ugly since it includes the prime factor 7.