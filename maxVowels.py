# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Using sliding window technique
# Time complexity: O(N)


def maxVowels(s, k):
    count = 0
    maxCount = -float('inf')
    vowels ="aeiou"
    for i, v in enumerate(s):
        if i >= k:
            if s[i - k] in vowels:
                count -= 1
        if v in vowels:
            count += 1 
        maxCount = max(maxCount, count)
    return maxCount

print(maxVowels("abciiidef", 3)) # Output: 3, Explanation: The substring "iii" contains 3 vowel letters.
print(maxVowels("aeiou", 2)) # Output: 2, Explanation: Any substring of length 2 contains 2 vowels.
print(maxVowels("leetcode", 3)) # Output: 2, Explanation: "lee", "eet" and "ode" contain 2 vowels.