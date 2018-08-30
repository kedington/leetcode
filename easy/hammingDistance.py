# Question : 461
# Time : O(1)
# Space : O(1)
# Runtime : 36 ms Your runtime beats 100.00% of python3 submissions lol

class Solution:
    #Too Easy
    def hammingDistance(self, x, y):
        return bin(x ^ y).count("1")

