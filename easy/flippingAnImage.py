# Question : 819                                                                               # Time : O(A)
# Space : O(A)
# Runtime : 60 ms

class Solution:
    def flipAndInvertImage(self, A):
        result = []
        for list in A:
            new_list = []
            for num in list:
                new_list.insert(0, int(not num))
            result.append(new_list)
        return result
