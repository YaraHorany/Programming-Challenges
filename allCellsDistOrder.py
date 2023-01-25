"""
You are given four integers row, cols, rCenter, and cCenter. 
There is a rows x cols matrix and you are on the cell with the coordinates (rCenter, cCenter).

Return the coordinates of all cells in the matrix, 
sorted by their distance from (rCenter, cCenter) from the smallest distance to the largest distance. 
You may return the answer in any order that satisfies this condition.

The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.
"""


def allCellsDistOrder(rows, cols, rCenter, cCenter):
	def sort_by_distance(coordinates):
		return abs(coordinates[0] - rCenter) + abs(coordinates[1] - cCenter)

	res = [[i, j] for i in range(rows) for j in range(cols)]

	return sorted(res, key=sort_by_distance)
	

print(allCellsDistOrder(1, 2, 0, 0)) # output: [[0,0],[0,1]], Explanation: The distances from (0, 0) to other cells are: [0,1]
print(allCellsDistOrder(2, 2, 0, 1)) # output: [[0,1],[0,0],[1,1],[1,0]]
print(allCellsDistOrder(2, 3, 1, 2)) # output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]