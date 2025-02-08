# Question : 387
# Difficulty : Easy
# Time : O(n)
# Space : O(n)
# Runtime : 51 ms

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_counts = Counter(s)
        for idx, c in enumerate(s):
            if char_counts[c] == 1:
                return idx
        return -1
