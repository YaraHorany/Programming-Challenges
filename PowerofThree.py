# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

# space complexity: O(1)

def isPowerOfThree(n):
	while n > 0:
		if n == 1: 
			return True
		n /= 3
	return False

print(isPowerOfThree(27)) # expected output: True
print(isPowerOfThree(0)) # expected output: False
print(isPowerOfThree(-1)) # expected output: False

