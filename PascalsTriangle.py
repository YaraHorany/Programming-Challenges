# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Constraints: 1 <= numRows <= 30

def generate(numRows):
	pascalList = list()
	pascalList.append([1])
	
	for row in range(numRows - 1):
		tempList = []
		for i in range(row + 2):
			if i == 0 or i == row + 1: # each row starts and ends with 1
				tempList.append(1)
			else:
				tempList.append(pascalList[len(pascalList) - 1][i-1]+pascalList[len(pascalList) - 1][i])
		pascalList.append(tempList)
	return pascalList



print(generate(6)) # expected output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1]]
print(generate(1)) # expected output: [[1]]