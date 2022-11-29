# Given an array of strings nums containing n unique binary strings each of length n, 
# return a binary string of length n that does not appear in nums. 
# If there are multiple answers, you may return any of them.

def findDifferentBinaryString(nums):
    for num in range(0,2**(len(nums))):
        strNum = str(bin(num)[2:])
        diff = len(nums) - len(strNum)
        if diff > 0:
        	strNum = ("0" * diff) + strNum
        if strNum not in nums:
            return strNum


print(findDifferentBinaryString(["01","10"])) # output: "11" , Explanation: "11" does not appear in nums. "00" would also be correct.
print(findDifferentBinaryString(["00","01"])) # output: "11" , Explanation: "11" does not appear in nums. "10" would also be correct.
print(findDifferentBinaryString(["111","011","001"])) # output: "101" , Explanation: "101", "000", "010", "100", and "110" does not appear in nums.