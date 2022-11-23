"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

"""
Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


def isPalindrome(s):
	s = s.lower() # convert all uppercase characters into lowercase characters
	s = ''.join(filter(str.isalnum, s)) # Filter only alpha-numeric characters from a string

	# using to pointers 
	i = 0
	j = len(s) - 1
	while i < j:
		if s[i] != s[j]:
			return False
		i += 1
		j -= 1
	return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))