"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""

#Constraints:

#1 <= s.length <= 105
#s[i] is a printable ascii character.

def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """ 
    i = len(s) - 1
    for j in range(0, int(len(s)/2)):
        s[j], s[i] = s[i], s[j]
        i -= 1
    print(s)

reverseString(["h","e","l","l","o"])
reverseString(["H","a","n","n","a","h"])
