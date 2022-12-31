"""
1539. Kth Missing Positive Number

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.
"""

def findKthPositive(arr, k):
    num = 1
    i = 0
    while k > 0 and i < len(arr):
        if arr[i] != num:
            k -= 1
        else: 
            i += 1
        num += 1
    if i >= len(arr):
        return num + k - 1
    return num - 1


print(findKthPositive([2,3,4,7,11], 5)) # Output: 9, Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
print(findKthPositive([1,2,3,4], 2)) # Output: 6, Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
print(findKthPositive([1,2], 1)) # Output: 3, Explanation: The missing positive integers are [3,4,...]. The 1st missing positive integer is 3.