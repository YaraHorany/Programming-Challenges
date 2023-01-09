"""
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.
"""


def longestMountain(arr):
    if len(arr) < 3: return 0
    
    start_i = -1
    new_mountain = True
    max_len = 0

    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            new_mountain = True
            start_i = -1

        elif arr[i] < arr[i + 1] and new_mountain:
            new_mountain = False
            start_i = i

        elif arr[i] > arr[i + 1] and start_i != -1:
            new_mountain = True
            max_len = max(max_len, i - start_i + 2)

    return max_len


print(longestMountain([2,1,4,7,3,2,5])) # output: 5, Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
print(longestMountain([2,2,2])) # output: 0, Explanation: There is no mountain.
print(longestMountain([0,2,0,2,1,2,3,4,4,1])) # output: 3
print(longestMountain([0,2,0,0,2,0,2,1,1,0,2,1,0,0])) # output: 4
print(longestMountain([0,2,0,0,2,0,2,1,1,0,2,1,0,0,1,0,2,1,2,0,1,1,0,2,2,1,2,2,0,0,0,1,0,2,0,0,1,2,0,1,0,2,0,2,0,0,0,0,2,1,0,0,0,0,1,0,2,1,2,2,1,0,0,1,0,2,0,0,0,2,1,0,1,2,1,0,1,0,2,1,0,2,0,2,1,1,2,0,1,0,1,1,1,1,2,1,2,2,2,0])) # output: 5