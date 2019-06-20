# Question : 448                                                                
# Difficulty : Easy
# Time : O(n)
# Space : O(n)
# Runtime : 140 ms

class Solution:
    def findDisappearedNumbers(self, nums: 'List[int]') -> 'List[int]':
        foo = set(range(1,len(nums)+1))
        for num in nums:
            if num in foo:
                foo.remove(num)
        return list(foo)
