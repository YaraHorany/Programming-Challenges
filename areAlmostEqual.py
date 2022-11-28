"""
You are given two strings s1 and s2 of equal length. 
A string swap is an operation where you choose two indices in a string (not necessarily different) 
and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. 
Otherwise, return false.
"""


def areAlmostEqual(s1, s2):
	first = -1
	second = -1
	if s1 == s2: # if we don't have to swap anything, they are equal then just return true
		return True
	for i in range(len(s1)):
		if s1[i] != s2[i] and first == -1:
			first = i
		elif s1[i] != s2[i] and second == -1:
			second = i
		elif s1[i] != s2[i]: # if there are three letters or more that are not equal, return false
			return False
	s1 = s1[:first] + s1[second] + s1[first+1:second] + s1[first] + s1[second+1:] # swap
	return s1 == s2



print(areAlmostEqual("bank", "kanb")) # expected output: True
print(areAlmostEqual("attack", "defend")) # expected output: False
print(areAlmostEqual("kelb", "kelb")) # expected output: True

