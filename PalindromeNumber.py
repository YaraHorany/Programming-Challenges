# Write a function that returns true if a number is a palindrome, else it returns false

def isPalindrome(num):
	original = num
	rev = 0
	while num > 0:
		rev = (rev * 10) + (num % 10)
		num /= 10
		num = int(num)
	return rev == original

print(isPalindrome(71234321)) # expected output: False
print(isPalindrome(712343217)) # expected output: True
print(isPalindrome(1)) # expected output: True