"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. 
The list must not contain the same combination twice, and the combinations may be returned in any order.

Constraints:
2 <= k <= 9
1 <= n <= 60

Example:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
"""

def combinationSum3(k, n):
	result = list()

	def backtracking(k , helpArr, comb):
		duplicate = False
		if sum(comb) == n and k == 0:
			for res in result: # checking if the same combination was alredy added to the final result.
				equal = [x for x in res + comb if x not in res or x not in comb]
				if not equal: 
					duplicate = True
					break
			if duplicate == False:
				result.append(list(comb))

		if k == 0:
			return

		for i in range(0, len(helpArr)):
			if helpArr[i] + sum(comb) <= n:
				comb.append(helpArr[i])
				backtracking(k - 1, helpArr[:i] + helpArr[i+1:], comb)
				comb.pop()

	comb = list()
	helpArr = [1,2,3,4,5,6,7,8,9]
	backtracking(k, helpArr, comb)
	return result
		

print(combinationSum3(3, 7)) # expected output: [[1,2,4]]
print(combinationSum3(3, 9)) # expected output: [[1,2,6],[1,3,5],[2,3,4]]
print(combinationSum3(4, 1)) # expected output: []