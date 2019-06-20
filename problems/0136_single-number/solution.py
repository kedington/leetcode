# Question : 136
# Difficulty : Easy
# Time : O(n)
# Space : O(1)
# Runtime : 30 ms

class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        a = 0
        for i in nums:
            a ^= i
        return a

# Single number in this case is found with XOR 
# Can also be found by 2 * sum(set(nums)) - sum(nums)
