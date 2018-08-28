# Question : 771
# Time : O(S)
# space : O(J)
# Runtime : 40 ms

class Solution:
    #Using a set for quick lookup
    def numJewelsInStones(self, J, S):
        jewels = set([j for j in J])
        count = 0
        for s in S:
            if s in jewels:
                count += 1
        return count
