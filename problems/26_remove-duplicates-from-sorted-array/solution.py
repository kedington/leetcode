# Question : 26
# Difficulty : Easy
# Time : O(n)
# Space : O(1)
# Runtime : 76 ms

class Solution:
    #Too easy
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i+1]
            else:
                i += 1
        return len(nums)
