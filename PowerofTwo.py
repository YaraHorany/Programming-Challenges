# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Follow up: Could you solve it without loops/recursion?

# Constraints: -231 <= n <= 231 - 1

import math

def isPowerOfTwo(n):
    if n <= 0:
        return False
    return math.log2(n) - int(math.log2(n)) == 0


print(isPowerOfTwo(16)) # output: True
print(isPowerOfTwo(1)) # output: True
print(isPowerOfTwo(3)) # output: False
print(isPowerOfTwo(-16)) # output: False