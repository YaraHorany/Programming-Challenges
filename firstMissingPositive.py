# Given an unsorted integer array nums, return the smallest missing positive integer.

# You must implement an algorithm that runs in O(n) time and uses constant extra space.


def firstMissingPositive(nums):
    setNums = set(nums) # remove duplicates
    nums = list(setNums) 
    nums.sort() # sort the list
    i = 0
    while i < len(nums) and nums[i] <= 0: # remove negatives and zero
        i += 1
    nums = nums[i:] # keep the positive numbers
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
            break
    return len(nums) + 1


print(firstMissingPositive([1,2,0])) # output: 3, Explanation: The numbers in the range [1,2] are all in the array.
print(firstMissingPositive([3,4,-1,1])) # output: 2, Explanation: 1 is in the array but 2 is missing.
print(firstMissingPositive([7,8,9,11,12])) # output: 1, Explanation: The smallest positive integer 1 is missing.
