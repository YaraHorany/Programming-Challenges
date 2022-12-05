# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

# Time complexity is O(NlogN)

def maximumProduct(nums):
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[-1] * nums[0] * nums[1])


print(maximumProduct([1,2,3])) # output: 6
print(maximumProduct([1,2,3,4])) # output: 24
print(maximumProduct([-1,-2,-3])) # output: -6
print(maximumProduct([-1,-2,-3,-4])) # output: -6
print(maximumProduct([-100,-98,-1,2,3,4])) # output: 39200
print(maximumProduct([0,-1,2,3])) # output 0



