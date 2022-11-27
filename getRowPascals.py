# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# Constraints: 0 <= rowIndex <= 33

def getRow(rowIndex):
	if rowIndex == 0:
		return [1]

	prevRow = [1]

	for i in range(rowIndex):
		row = []
		for j in range(i + 2):
			if j == 0 or j == i + 1: # each row starts and ends with 1
				row.append(1)
			else:
				row.append(prevRow[j-1]+prevRow[j])
		prevRow = row
	return prevRow

print(getRow(3)) # expected output: [1,3,3,1]
print(getRow(0)) # expected output: [1]
print(getRow(1)) # expected output: [1,1]