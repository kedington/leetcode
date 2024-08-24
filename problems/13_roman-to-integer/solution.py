# Question : 13 
# Difficulty : Easy
# Time : O(n)
# Space : O(1)
# Runtime : 54 ms

roman_numerals = {"I" : 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
out_of_order_char = ["I", "X", "C"]

class Solution:
    def romanToInt(self, s: str) -> int:
        prev_char = ""
        running_total = 0
        for char in s:
            current_val = roman_numerals[char]
            if prev_char and prev_char in out_of_order_char and roman_numerals[prev_char] < current_val:
                 current_val = current_val - (roman_numerals[prev_char] * 2)
            running_total += current_val
            prev_char = char
        return running_total
