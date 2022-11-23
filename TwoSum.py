"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        finalNums = []

        for i in range(0, len(nums)):
            if nums.count(target - nums[i]) > 0 and nums.index(target - nums[i]) != i:
                print(target - nums[i])
                finalNums.append(i)
                finalNums.append(nums.index(target - nums[i]))
                break
        return finalNums
        