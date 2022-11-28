# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.



def findLength(nums1, nums2):
    dp = [[0]*(len(nums1)+1) for i in range(len(nums2)+1)]
    max_count = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                dp[i][j] = dp[i-1][j-1]+1
                max_count = max(max_count,dp[i][j])
    print(dp)
    return max_count

print(findLength([1,2,3,2,1], [3,2,1,4,7])) # expected output: 3
print(findLength([0,0,0,0,0], [0,0,0,0,0])) # expected output: 5