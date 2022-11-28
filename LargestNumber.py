# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

# Constraints: 1 <= nums.length <= 100 , 0 <= nums[i] <= 109

def largestNumber(nums):
    str_nums = []
    for num in nums:
        str_nums.append(str(num)) # turn numbers to strings
    
    flag = False # flag to keep track if there were swaps, if no more swaps needed - finished
    while not flag:
        flag = True
        i=0
        while i < len(str_nums)-1:
            if str_nums[i]+str_nums[i+1] < str_nums[i+1]+str_nums[i]: # if larger when swapped - swap
                str_nums[i], str_nums[i+1] = str_nums[i+1], str_nums[i]
                flag = False
            i += 1
            
    res = "".join(str_nums)
    
    if res[0] == '0':
        return str(0)
    
    return res


print(largestNumber([909, 98,93,15,9])) # expected output: "9989390915"
print(largestNumber([3,30,34,5,9])) # expected output: "9534330"
print(largestNumber([9,9])) # expected output: "99"
print(largestNumber([111311, 1113])) # expected output: "1113111311"