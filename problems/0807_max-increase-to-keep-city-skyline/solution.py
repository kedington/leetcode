# Question : 807
# Difficulty : Medium
# Time : O(n)
# Space : O(n)
# Runtime : 70 ms

class Solution:
    #BruteForce
    def maxIncreaseKeepingSkyline(self, grid):
        gridLength = len(grid)
        maxRow = 0
        maxColumn = 0
        maxRowList = []
        maxColumnList = []
        for i in range(gridLength):
            for j in range(gridLength):
                if grid[i][j] > maxRow:
                    maxRow = grid[i][j]
            maxRowList.append(maxRow)
            maxRow = 0
        for j in range(gridLength):
            for i in range(gridLength):
                if grid[i][j] > maxColumn:
                    maxColumn = grid[i][j]
            maxColumnList.append(maxColumn)
            maxColumn = 0
        count = 0
        for i in range(gridLength):
            for j in range(gridLength):
                count += (min(maxRowList[i], maxColumnList[j]) - grid[i][j])
        return count
