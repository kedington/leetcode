# Question : 268
# Difficulty : Easy
# Time : O(n)
# Space : O(1)
# Runtime : 10 ms

class Solution(object):
    def missingNumber(self, nums):
        count = 0
        for num in nums:
            count += num
        return sum(range(len(nums)+1)) - count
