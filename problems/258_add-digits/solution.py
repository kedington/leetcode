# Question : 258    
# Difficulty : Easy 
# Time : O(1)
# Space : O(1)
# Runtime : 45 ms

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return num % 9 if num % 9 else 9
