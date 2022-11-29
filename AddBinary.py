# Given two binary strings a and b, return their sum as a binary string.

def addBinary(a, b):
    diff = 0
    c = ""
    length = min(len(a), len(b))
    if len(a) != len(b):
        diff = len(a) - len(b) # if diff is positive then a's length is greater than b's length, if length is negative then length of b is greater
    temp = 0
    for i in range(1, length + 1):
        if (int(a[-i]) + int(b[-i]) + temp) % 2 == 1:
            c = "1" + c
        elif (int(a[-i]) + int(b[-i]) + temp) % 2 == 0:
            c = "0" + c
        if (int(a[-i]) + int(b[-i]) + temp) >= 2:
            temp = 1
        else: temp = 0
    if diff == 0:
        if temp == 1:
            c = "1" + c
    else:
        if diff > 0: # a's length is greater than b's length
            if temp == 0:
                c = a[0:diff] + c
            else:
                while diff > 0:
                    if int(a[diff - 1]) + temp == 2:
                        temp = 1
                        c = "0" + c
                    elif int(a[diff - 1]) + temp == 1:
                        temp = 0
                        c = "1" + c
                    elif int(a[diff - 1]) + temp == 0:
                        temp = 0
                        c = "0" + c
                    diff -= 1
                if temp == 1:
                    c = "1" + c

        else: # diff < 0
            diff = abs(diff)
            if temp == 0:
                c = b[0:diff] + c 
            else:
                while diff > 0:
                    if int(b[diff - 1]) + temp == 2:
                        temp = 1
                        c = "0" + c
                    elif int(b[diff - 1]) + temp == 1:
                        temp = 0
                        c = "1" + c
                    elif int(b[diff - 1]) + temp == 0:
                        temp = 0
                        c = "0" + c
                    diff -= 1
                if temp == 1:
                    c = "1" + c
    return c

print(addBinary("11", "1")) # expected output: "100"
print(addBinary("1010", "1011")) # expected output: ""10101""
print(addBinary("100", "110010")) # expected output: "110110"
