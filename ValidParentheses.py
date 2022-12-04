# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# solution using stack

def isValid(s):
    if len(s) % 2 == 1: return False
    stack = []
    right = ['(','{','[']
    for i in range(len(s)):
        if s[i] in right:
            stack.append(s[i])
        else:
            if len(stack) > 0:
                c = stack.pop()
                if (s[i] == ')' and c != '(') or (s[i] == '}' and c != '{') or (s[i] == ']' and c != '['):
                    return False
            else: return False
    if len(stack) != 0: return False
    return True


    # i = 0
    # while i < len(s) - 1:
    #     if (s[i] == '(' and s[i+1] == ')') or (s[i] == '{' and s[i+1] == '}') or (s[i] == '[' and s[i+1] == ']'):
    #         s = s[:i] + s[i+2:]
    #         if i != 0:
    #             i -= 1
    #     else: i += 1
    # return s == ""


print(isValid("()")) # output: True
print(isValid("()[]{}")) # output: True
print(isValid("{()}")) # output: True
print(isValid("((({{([[]])}})))")) # output: True
print(isValid("([)]")) # output: False
print(isValid("(]")) # output: False
