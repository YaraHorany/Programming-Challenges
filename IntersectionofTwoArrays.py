"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        finalNums = []

        if len(nums1) <= len(nums2):
            for num in nums1:
                if nums2.count(num) > 0:
                    finalNums.append(num)
                    nums2[nums2.index(num)] = -1
        else:
            for num in nums2:
                if nums1.count(num) > 0:
                    finalNums.append(num)
                    nums1[nums1.index(num)] = -1
                    
        return finalNums