# Question : 28
# Difficulty : Easy
# Time : O(n)
# Space : O(1)
# Runtime : 40 ms

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pointer = 0
        needle_len = len(needle)
        while pointer + needle_len < len(haystack)+1:           
            if needle == haystack[pointer:pointer+needle_len]:
                    return pointer
            pointer += 1
        return -1
