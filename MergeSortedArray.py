"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""

# Time complexity: O(n+m)
# Space complexity: O(1)

def merge(nums1, m, nums2, n):
	# Using 2 pointers for each array
    j = 0
    i = 0
    while i < m + j and j < n:
        if nums2[j] < nums1[i]:
            nums1.insert(i, nums2[j]) # bring a value from nums2
            nums1.pop(-1) # remove one zero
            j += 1
        i += 1

    while j < n: # if the second array still has some values then just add them to the first array
        nums1.insert(i, nums2[j])
        nums1.pop(-1)
        i += 1
        j += 1


merge([3,4,5,0,0], 3, [1,2], 2) # expected output: [1,2,3,4,5]
merge([1,2,3,0,0,0], 3, [2,5,6], 3) # expected output: [1,2,2,3,5,6]
merge([1], 1, [], 0) # expected output: [1]
merge([0], 0, [1], 1) # expected output: [1]
merge([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3) # expected output: [-1,0,0,1,2,2,3,3,3]
