"""
Your friend is typing his name into a keyboard. 
Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. 
Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.
"""


def isLongPressedName(name, typed):
    i = 0
    j = 0

    while i < len(name) and j < len(typed):
        count1 = 1
        count2 = 1

        if name[i] == typed[j]:

            while i != len(name) - 1 and name[i] == name[i+1]:
                i += 1
                count1 += 1

            while j != len(typed) - 1 and typed[j] == typed[j+1]:
                j += 1
                count2 += 1

            if count1 > count2:
                return False

        else: 
        	return False

        i += 1
        j += 1

    if i < len(name) or j < len(typed): return False
    return True

print(isLongPressedName("alex", "aaleex")) # Output: True
print(isLongPressedName("alex", "aaleexa")) # Output: False
print(isLongPressedName("saeed", "ssaaedd")) # Output: False