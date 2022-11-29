"""
You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of digit from number 
such that the value of the resulting string in decimal form is maximized. 
The test cases are generated such that digit occurs at least once in number.

Example:

Input: number = "1231", digit = "1"
Output: "231"
Explanation: We can remove the first '1' to get "231" or remove the second '1' to get "123".
Since 231 > 123, we return "231".
"""


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxNum = -float("inf")
        countDigit = number.count(digit)
        if countDigit == 1:
            return number[:number.index(digit)] + number[number.index(digit) + 1:]
        for i in range(len(number)):
            if number[i] == digit:
                maxNum = max(maxNum, int(number[:i] + number[i + 1:]))
        return str(maxNum)