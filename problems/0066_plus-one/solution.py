# Question : 66
# Difficulty : Easy
# Time : O(n)
# Space : O(1)
# Runtime : 36 ms

class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':  
        if not digits:
            return [1]
        for idx in range(len(digits)-1, -1, -1):
            if digits[idx] < 9:
                digits[idx] += 1
                break
            else:
                digits[idx] = 0
                if idx == 0:
                    digits = [1] + digits
        return digits

