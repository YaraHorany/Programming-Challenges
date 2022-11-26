# Given an integer array nums, find the subarray which has the largest sum and return its sum.

"""
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

import math

# Time complexity: O(N)

def maxSubArray(nums):
	newSum = maxSum = nums[0]        
	for i in range(1, len(nums)):
		newSum = max(nums[i], nums[i] + newSum)
		maxSum = max(newSum, maxSum)

	return maxSum

print(maxSubArray([4,5,-6,-7,10,2])) # expected output: 12
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # expected output: 6 
print(maxSubArray([5,4,-1,7,8])) # expected output: 23
print(maxSubArray([1])) # expected output: 1
print(maxSubArray([-1])) # expected output: -1

# Time complexity: O(N*N)

# def maxSubArray(nums):
# 	sumArr = -math.inf
# 	subArr = []
# 	k = len(nums)
# 	while k > 0:
# 		for i in range(0, len(nums) - (k - 1)):
# 			subArr = nums[i:i+k]
# 			if sum(subArr) > sumArr:
# 				sumArr = sum(subArr)
# 		k -= 1
# 	print(sumArr)
	
