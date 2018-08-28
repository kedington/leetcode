# Question : 27
# Time : O(n)
# Space : O(1)
# Runtime : 40 ms

class Solution:
    #While loop solution
    def removeElement(self, nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
            
