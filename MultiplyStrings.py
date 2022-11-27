"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example:

Input: num1 = "123", num2 = "456"
Output: "56088"
"""

import math

def multiply(num1, num2):
	temp = 0
	result = 0
	finalResult = 0

	# calculate the integer multiplication
	for i in range(0, len(num2)):
		intNum2 = int(num2[-1 *(i + 1)]) 
		for j in range(0, len(num1)): 
			intNum1 = int(num1[-1 *(j + 1)]) 
			mult = (intNum1 * intNum2) + temp
			result = result + ((mult % 10) * (10 ** j))
			temp = int(mult / 10)	
		if temp > 0:
			result += temp * (10 ** (j + 1))
		finalResult += (result * 10 ** i)
		result = 0
		temp = 0

	return str(finalResult)

print(multiply("0", "0")) # Output: "0"
print(multiply("123","456")) # Output: "56088"
print(multiply("9234","456")) # Output: "4210704"
print(multiply("6913259244","71103343")) # output: "491555843274052692"