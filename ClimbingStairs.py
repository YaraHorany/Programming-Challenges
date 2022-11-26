"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Constraints: 1 <= n <= 45

Example:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""

import math

def climbStairs(n):
	ways = 0
	numTwo = int(n / 2)
	while numTwo >= 0:
		numOne = n - (numTwo * 2)
		ways += math.comb(numTwo + numOne, numTwo) # 𝑛!/(𝑘!(𝑛−𝑘)!
		numTwo -= 1
	return ways

print(climbStairs(3)) # expected output: 3
print(climbStairs(7)) # expected output: 21
print(climbStairs(8)) # expected output: 34