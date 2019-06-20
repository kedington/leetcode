# Question : 665
# Difficulty : Easy
# Time : O(n)
# Space : O(1)
# Runtime : 56 ms

class Solution:
    def isIncreasing(self, nums):
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                return False
        return True
        
    #Brute Force crappy solution
    def checkPossibility(self, nums):
        for i in range(0, len(nums)-2):
            if nums[i] > nums[i+1]:
                if i > 0:
                    if nums[i-1] > nums[i+1]:
                        del nums[i+1]
                        del nums[:i-1]
                        return self.isIncreasing(nums)
                del nums[i]
                if i > 1:
                    del nums[:i-2]
                return self.isIncreasing(nums)
        return True
