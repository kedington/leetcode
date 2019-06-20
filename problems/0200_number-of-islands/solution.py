# Question : 200
# Difficulty : Medium
# Time : O(n^2)
# Space : O(1)
# Runtime : 100 ms

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        stack = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == '1':
                    num += 1
                    stack.append((x, y))
                    while stack:
                        idx = stack.pop()
                        if grid[idx[1]][idx[0]] == '1':
                            grid[idx[1]][idx[0]] = '0'
                            if 0 <= idx[0]-1 < len(grid[0]):
                                stack.append((idx[0]-1, idx[1]))
                            if 0 <= idx[0]+1 < len(grid[0]):
                                stack.append((idx[0]+1, idx[1]))
                            if 0 <= idx[1]-1 < len(grid):
                                stack.append((idx[0], idx[1]-1))
                            if 0 <= idx[1]+1 < len(grid):
                                stack.append((idx[0], idx[1]+1))
        return num
