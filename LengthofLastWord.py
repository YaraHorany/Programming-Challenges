# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

def lengthOfLastWord(s):
	arr = s.split()
	return len(arr[-1])

print(lengthOfLastWord("Hello World")) # Output: 5
print(lengthOfLastWord("   fly me   to   the moon  ")) # Output: 4
print(lengthOfLastWord("luffy is still joyboy")) # Output: 6