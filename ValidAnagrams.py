# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Runtime = O(n)
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    for ch in s:
        if s.count(ch) != t.count(ch):
            return False
    return True

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
print(isAnagram("angered", "enraged"))