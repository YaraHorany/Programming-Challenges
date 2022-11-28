# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
# whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


def minSubArrayLen(target, nums):
	start = 0
	end = 0
	currentSum = 0
	minLength = float('inf')
	while end < len(nums):
		currentSum += nums[end]
		end += 1

		while start < end and currentSum >= target:
			currentSum -= nums[start]
			start += 1

			minLength = min(minLength, end - start + 1)
	if minLength == float('inf'):
		minLength = 0
	return minLength



print(minSubArrayLen(7, [2,3,1,2,4,3])) # Output: 2 , The subarray [4,3] has the minimal length under the problem constraint.
print(minSubArrayLen(4, [1,4,4])) # Output: 1
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1])) # Output: 0
print(minSubArrayLen(11, [1,2,3,4,5])) # Output: 3