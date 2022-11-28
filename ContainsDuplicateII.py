# Given an integer array nums and an integer k, 
# return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


def containsNearbyDuplicate(nums, k):
	index_dict = {}

	for i, num in enumerate(nums):
		if num in index_dict and (i - index_dict[num] <= k):
			return True
		index_dict[num] = i

	return False

print(containsNearbyDuplicate([1,2,3,1], 3)) # expected output: True
print(containsNearbyDuplicate([1,2,3,1,2,3], 2)) # expected output: False
print(containsNearbyDuplicate([1,0,1,1], 1)) # expected output: True