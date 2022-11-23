"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

# Constraints:
# -231 <= x <= 231 - 1

def reverse(x):
    pos = True

    if x < 0: # pos is a boolean variable, if the number is negative then pos is equal to false
        pos = False

    x = abs(x)

    y = 0

    for i in range(len(str(x)) - 1, -1, -1):
        y += (x%10) * pow(10, i)
        x = int(x/10)

    if pos == False:
        y = -abs(y)

    if abs(y) >= 2**31:
        return 0
    else:
        return y


print(f'123 ---> {reverse(123)}')
print(f'-123 ---> {reverse(-123)}')
print(f'120 ---> {reverse(120)}')