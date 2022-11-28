# Given an integer array nums, return the third distinct maximum number in this array. 
# If the third maximum does not exist, return the maximum number.


def thirdMax(nums):
    k = 2
    nums.sort()

    if len(nums) < 3:
        return nums[-1]
        
    else: 
    	i = len(nums) - 2
    	while i >= 0 and k > 0:
    		if nums[i] != nums[i+1]:
    			k -= 1
    		i -= 1
    	if k != 0: # the third maximum does not exist so return the maximum number (last number in the sorted array)
    		return nums[-1]
    	else:
    		return nums[i+1]

print(thirdMax([3,2,1])) # output: 1
print(thirdMax([1,2])) # output: 2
print(thirdMax([2,2,3,1])) # output: 1

