# Question : 412
# Difficulty : Easy
# Time : O(n)
# Space : O(1)
# Runtime : 70 ms


class Solution:
    def fizzBuzz(self, n):
        l = []
        for num in range(1, n+1):
            if num % 3 == 0 and num % 5 == 0:
                l.append("FizzBuzz")
            elif num % 3 == 0:
                l.append("Fizz")
            elif num % 5 == 0:
                l.append("Buzz")
            else:
                l.append(str(num))
        return l
