"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses 
have security systems connected and it will automatically contact the police if 
two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400

Example:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""

def rob(nums):
	if len(nums) <= 2: # length is equal to 1 or 2
		return max(nums)

	cal = [nums[0], max(nums[0], nums[1])]

	for index, num in enumerate(nums[2:], 2):
		cal.append(max(cal[index - 1], cal[index - 2] + num))

	return cal[-1]

print(rob([2,7,9,3,1])) # expected output: 12
print(rob([1,5,12,3,25,4,8,6,9,15,30]))
print(rob([2,1,1,2]))
print(rob([1]))


	# maxAmount1 = maxAmount2 = 0
	# for i in range(0, len(nums)):
	# 	if i % 2 == 0:
	# 		maxAmount1 += nums[i]
	# 	else:
	# 		maxAmount2 += nums[i]	
	# return max(maxAmount1,maxAmount2)	
