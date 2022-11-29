# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# Constraints: 0 <= num <= 231 - 1

# Follow up: Could you do it without any loop/recursion in O(1) runtime?

# Time complexity: O(1)

def addDigits(num):
    if int(num/10) == 0:
        return num
    numList = list(map(int, str(num)))
    num = sum(numList)
    if int(num/10) == 0:
        return num
    numList = list(map(int, str(num)))
    num = sum(numList)
    if int(num/10) == 0:
        return num
    numList = list(map(int, str(num)))
    num = sum(numList)
    if int(num/10) == 0:
        return num

print(addDigits(38)) # output: 2, Explanation: The process is 38 --> 3 + 8 --> 11, 11 --> 1 + 1 --> 2
print(addDigits(0)) # output: 0