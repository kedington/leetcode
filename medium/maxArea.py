# Question : 11
# Time : O(n)
# Space : O(1)
# Runtime : 60 ms

class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        start = 0
        end = len(height) - 1
        largest = 0
        while start < end:
            curr = min(height[start], height[end]) * (end-start)
            if height[start] < height[end]:
                start += 1
            elif height[start] > height[end]:
                end -= 1
            else:
                start += 1
                end -= 1
            largest = max(largest, curr)
        return largest
