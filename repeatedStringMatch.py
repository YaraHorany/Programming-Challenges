"""
Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. 
If it is impossible for b to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".
"""


def repeatedStringMatch(a, b):
	if len(a) > len(b):
		if b in a: return 1
		if b in a * 2: return 2

	count = 0
	
	while (count * len(a)) <= 2 * len(b):
		count += 1
		if b in count * a:
			return count

	return -1


print(repeatedStringMatch("abcd", "cdabcdab")) # Output: 3, Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.
print(repeatedStringMatch("abcbc", "cabcbca")) # 3
print(repeatedStringMatch("a", "aa")) # Output: 2
print(repeatedStringMatch("aa", "a")) # Output: 1
print(repeatedStringMatch("aaaaaaaaaaaaaaaaaaaaaab", "ba")) # Output: 2
