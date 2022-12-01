# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
# The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.



# The binary search was implemented, time complexity: O(log n)

def mySqrt(x):
    if x == 0 or x == 1:
        return x
    low = 1
    high = x // 2 + 1
    while high - low > 1:
        mid = (low + high) // 2
        if mid * mid > x:
            high = mid
        elif mid * mid < x:
            low = mid
        else:
            return mid
    return low


print(mySqrt(4)) # output: 2, Explanation: The square root of 4 is 2, so we return 2.
print(mySqrt(8)) # output: 2, Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

