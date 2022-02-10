# Question : 532
# Difficulty : Medium
# Time : O(n)
# Space : O(n)
# Runtime : 72  ms

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen = set()
        count = 0
        doubled = set()
        for val in nums:
            if val in seen:
                if val - val == k and val not in doubled:
                    count += 1
                    doubled.add(val)
                continue
            if val - k in seen:
                count += 1
            if val + k in seen:
                count += 1
            seen.add(val)
        return count
        
