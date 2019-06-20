# Question : 35 
# Difficulty : Easy
# Time : O(log(n))
# Space : O(1)
# Runtime : 40 ms

class Solution:
    #Binary Search
    def searchInsert(self, nums, target):
        return self.binarySearch(nums, target, 0)
        
    def binarySearch(self, nums, target, pos):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            if target <= nums[0]:
                return pos
            else:
                return pos+1
        middle = int(len(nums)/2)
        if nums[middle-1] < target <= nums[middle]:
            return pos + middle
        if target <= nums[middle]:
            return self.binarySearch(nums[:middle], target, pos)
        else: 
            return self.binarySearch(nums[middle:], target, pos + middle)
