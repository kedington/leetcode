# Question : 15
# Time : O(n^2)
# Space : O(n^2)
# Runtime : 70 ms

class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        nums.sort()
        result = []
        result_set = set()
        for i in range(len(nums)-2):
            j = i+1 
            k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] + nums[i] == 0:
                    if (nums[i], nums[j], nums[k]) not in result_set:
                        result.append((nums[i], nums[j], nums[k]))
                        result_set.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] + nums[i] < 0:
                    j += 1
                else:
                    k -= 1
        return result 
