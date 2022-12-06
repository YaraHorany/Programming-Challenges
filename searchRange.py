# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


# I impelemented the binary search algorithm with O(log n) time complexity.

def searchRange(nums, target):
    if len(nums) == 0 or target not in nums: return [-1,-1]
    return [binary_search(nums, target), binary_search(nums, target + 1) - 1]

# if target is IN nums, it will return the first appearance of target in nums
# if target is NOT IN nums, it will return the index where it's suppose to be 
def binary_search(nums, target): 
    low = 0
    high = len(nums)
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < target:
        	low = mid + 1
        else:
        	high = mid
    return low

print(searchRange([5,7,7,8,8,8,8,10], 8)) # Expected output: [3,6]
print(searchRange([5,7,7,8,8,10], 8)) # Expected output: [3,4]
print(searchRange([5,7,7,8,8,10], 6)) # Expected output: [-1,-1]
print(searchRange([], 0)) # Expected output: [-1,-1]