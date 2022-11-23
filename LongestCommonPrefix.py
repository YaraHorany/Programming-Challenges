"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

"""

def longestCommonPrefix(strs):
    j = 0
    returnedStr = ''
    # find the string with the minimum length, that could be the longest prefix
    res = min(len(st) for st in strs) 
    while j < res:
        for i in range(0, len(strs) - 1):
            if strs[i][j] != strs[i+1][j]: # for all strings check the same index if it's the same
                return returnedStr
        returnedStr += strs[0][j]
        j += 1
    return returnedStr

print(longestCommonPrefix(["flow","flight","flower"]))
print(longestCommonPrefix(["dog","racecar","car"]))