"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""
"""
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
"""

def strStr(haystack, needle):
	
	# if needle in haystack:
	# 	for i in range(0, len(haystack)):
	# 		j = 0
	# 		k = i
	# 		while j < len(needle) and k < len(haystack) and haystack[k] == needle[j]:
	# 			k += 1
	# 			j += 1
	# 		if j >= len(needle):
	# 			return i
	# else:
	# 	return -1

	if needle in haystack: 
		return haystack.index(needle)
	else: 
		return -1

print(strStr("sadbutsad","sad"))
print(strStr("leetcode","leeto"))