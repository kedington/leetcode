# Question : 12
# Time : O(1)
# Space : O(1)
# Runtime : 100 ms

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        number_of_m = num // 1000
        roman += 'M' * number_of_m
        num -= 1000 * number_of_m
        if num >= 900:
            roman += 'CM'
            num -= 900
        elif num >= 500:
            roman += 'D'
            num -= 500
        elif num >= 400:
            roman += 'CD'
            num -= 400
        number_of_c = num // 100
        roman += 'C' * number_of_c
        num -= 100 * number_of_c
        if num >= 90:
            roman += 'XC'
            num -= 90
        elif num >= 50:
            roman += 'L'
            num -= 50
        elif num >= 40:
            roman += 'XL'
            num -= 40
        number_of_x = num // 10
        roman += 'X' * number_of_x
        num -= 10 * number_of_x
        if num >= 9:
            roman += 'IX'
            num -= 9
        elif num >= 5:
            roman += 'V'
            num -= 5
        elif num >= 4:
            roman += 'IV'
            num -= 4
        roman += 'I' * num
        return roman
