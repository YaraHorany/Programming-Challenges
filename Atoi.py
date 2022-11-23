"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.

Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
"""

def myAtoi(s):
    if len(s) == 0: # return 0 if it's an empty string
        return 0

    positive = True
    start = -1
    end = len(s)

    for i in range(0, len(s)):
        if s[i] == ' ':
            if start != -1:
                end = i
                break

        elif s[i] == '+' and start == -1:
            positive = True
            if i + 1 < len(s):
            	if s[i+1].isnumeric() == False: # if the '+' sign is NOT followed by a number then return 0
            		return 0
            else: # if the '+' sign is the last digit then return 0
            	return 0

        elif s[i] == '-' and start == -1:
            positive = False
            if i + 1 < len(s):
            	if s[i+1].isnumeric() == False: # if the '-' sign is NOT followed by a number then return 0
            		return 0
            else: # if the '-' sign is the last digit then return 0
            	return 0

        elif s[i].isnumeric():
            if start == -1:
            	# save the indexes
                start = i 
                end = i + 1
            else:
                end = i + 1

        else:
            if start == -1:
                return 0
            else:
                break

    if start != -1:
        s = s[start:end]
        s = int(s) # convert string to integer
        if positive == False:
            s *= -1

        if abs(s) >= 2**31:
            if positive == True:
                s = 2**31 - 1
            else:
                s = -2**31
    else: # if the string doesn't have any numbers
        return 0

    return s

print(myAtoi("42")) # expected: 42
print(myAtoi("   -42")) # expected: -42
print(myAtoi("4193 with words")) # expected: 4193
print(myAtoi("words and 987")) # expected: 0
print(myAtoi("+-12")) # expected: 0
print(myAtoi(" ")) # expected: 0
print(myAtoi("")) # expected: 0
print(myAtoi("3.14159")) # expected: 3
print(myAtoi("  +  413")) # expected: 0
print(myAtoi("+")) # expected: 0
