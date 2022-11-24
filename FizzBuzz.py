"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Example:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
"""

def fizzBuzz(n):
	strOutput = []
	for i in range(0, n):
		if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
			strOutput.append("FizzBuzz")
		elif (i + 1) % 3 == 0:
			strOutput.append("Fizz")
		elif (i + 1) % 5 == 0:
			strOutput.append("Buzz")
		else:
			strOutput.append(str(i+1))
	return strOutput

print(fizzBuzz(3)) # expected output: ["1","2","Fizz"]
print(fizzBuzz(5)) # expected output: ["1","2","Fizz","4","Buzz"]
print(fizzBuzz(15)) # expected output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
