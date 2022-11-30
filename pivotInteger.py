"""
Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. 
It is guaranteed that there will be at most one pivot index for the given input.
"""

# binary-search with O(log n) runtime complexity.

def pivotInteger(n):
	if n == 1:
		return 1
	low = 1
	high = n 
	sum1 = 0 
	sum2 = 0
	while high - low > 1:
		mid = (high + low) // 2
		sum1 = sum(list(range(1, mid + 1)))
		sum2 = sum(list(range(mid, n + 1)))
		if sum1 == sum2:
			return mid
		elif sum2 > sum1:
			low = mid
		else: # sum1 > sum2
			high = mid
	return -1


print(pivotInteger(8)) # output: 6, Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
print(pivotInteger(1)) # output: 1, Explanation: 1 is the pivot integer since: 1 = 1.
print(pivotInteger(4)) # output: -1, Explanation: It can be proved that no such integer exist.


