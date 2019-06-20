# Question : 14
# Time : O(n*len(strs))
# Space : O(1)
# Runtime : 36 ms

class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if not strs:
            return ""
        shortest = len(strs[0])
        for string in strs:
            shortest = min(shortest, len(string))
        if not shortest:
            return ""
        i = 0    
        for i in range(shortest):
            char = strs[0][i]
            for string in strs:
                if string[i] != char:
                    return strs[0][:i]    
        return strs[0][:i+1]
