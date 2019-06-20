# Question : 1
# Difficulty: easy
# Time : O(n)
# Size : O(N)
# Runtime: 40 ms 


class Solution:
    #one Pass dictionary
    def twoSum(self, nums, target):
        numbersToIndexs = {nums[0] : 0}
        for i in range(1, len(nums)):
            complement = target - nums[i]
            if complement in numbersToIndexs:
                return [numbersToIndexs[complement], i]
            else :
                numbersToIndexs[nums[i]] = i

