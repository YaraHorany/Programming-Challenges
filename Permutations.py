# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


def backtracking(nums, arr, answers):
    if len(nums) == 0:                      
        answers.append(list(arr))           

    for i in range(0 , len(nums)):
        arr.append(nums[i])
        backtracking(nums[:i] + nums[i+1:], arr, answers)             
        arr.pop()                               

def permute(nums):
    if len(nums) == 0:
        return answers
    
    arr = list()
    answers = list()

    backtracking(nums, arr, answers)
    
    return answers


print(permute([1,2,3])) # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(permute([0,1])) # Output: [[0,1],[1,0]]
print(permute([1])) # Output: [[1]]