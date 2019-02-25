# Question : 20
# Time : O(n)
# Space : O(n)
# Runtime : 36 ms

class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        stack = []
        for bracket in s:
            if bracket in bracket_map:
                if not stack:
                    return False
                if bracket_map[bracket] != stack.pop():
                    return False
            else:
                stack.append(bracket)
        return not stack 
