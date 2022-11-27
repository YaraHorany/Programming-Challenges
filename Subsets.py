"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

def subsets(nums):           
    res = list()
    backtracking(nums,[], res)
    return res

def backtracking(nums,path, res):    
    res.append(path)

    if not nums:
        return
    
    for i in range(len(nums)):
        backtracking(nums[i+1:],path+[nums[i]], res)


print(subsets([1,2,3])) # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(subsets([0])) # Output: [[],[0]]