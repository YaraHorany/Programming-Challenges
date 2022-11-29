# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


def searchInsert(nums, target):
	# we implemented the binary search with O(log n) runtime complexity.
    low = 0
    high = len(nums) - 1
    while low < high and low >= 0 and high >=0:
        mid = int((low + high) / 2)
        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
        else:
        	return mid # we found the target on the array, so just return it's index
    if target <= nums[low]:
    	return low
    else:
    	return low + 1


print(searchInsert([1,3,5,6], 5)) # expected output: 2
print(searchInsert([1,3,5,6], 2)) # expected output: 1
print(searchInsert([1,3,5,6], 7)) # expected output: 4
print(searchInsert([1,3,5,6], 0)) # expected output: 0
print(searchInsert([1,3,4,6], 5)) # expected output: 3
print(searchInsert([1], 1)) # expected output: 0
print(searchInsert([1,3], 0)) # expected output: 0
print(searchInsert([3,5,7,9,10], 8)) # expected output: 3
