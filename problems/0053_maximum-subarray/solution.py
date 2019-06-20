# Question : 53
# Difficulty : Easy
# Time : O(n)
# Size : O(1)
# Runtime: 50 ms 

class Solution:
    def maxSubArray(self, nums):
        if not len(nums):
            return None
        greatest = nums[0]
        current = greatest
        for num in nums[1:]:
            current += num
            if num > current:
                current = num 
            if current > greatest:
                greatest = current
        return greatest
