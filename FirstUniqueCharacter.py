# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

#Constraints:
#1 <= s.length <= 105
#s consists of only lowercase English letters.


# runtime: O(N)
def firstUniqChar(s):
    for char in s:
        if s.count(char) == 1:
            return s.index(char)
    return -1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))


