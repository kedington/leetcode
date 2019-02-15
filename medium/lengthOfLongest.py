# Question : 3
# Time : O(n)
# Space : O(n)
# Runtime : 76 ms

class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        str_len = len(s)
        longest = i = j = 0
        char_idx = dict()
        while j < str_len:
            if s[j] in char_idx:
                i = max(char_idx[s[j]], i)
            longest = max(longest, j-i + 1)
            char_idx[s[j]] = j + 1
            j += 1
        return longest
