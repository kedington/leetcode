# Question : 389
# Difficulty : Easy
# Time : O(n)
# Space : O(1)
# Runtime : 44 ms

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(ord(c) for c in t) - sum(ord(c) for c in s))

