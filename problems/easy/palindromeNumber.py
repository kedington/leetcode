# Question : 9
# Time : O(n)
# Space : O(1)
# Runtime : 264 ms

class Solution:
    # Convert to String
    def isPalindrome(self, x):
        xString = str(x)
        for i in range(0, int(len(xString)/2)):
            if xString[i] != xString[len(xString)-1-i]:
                return False
        return True
