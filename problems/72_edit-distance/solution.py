# Question : 72
# Difficulty : Hard
# Time : O(NxM)
# Space : O(NxM)
# Runtime : 200 ms

class Solution:
    def minDistance(self, word1: 'str', word2: 'str') -> 'int':
        len_str1 = len(word1)
        len_str2 = len(word2)

        result_matrix = [[0 for x in range(len_str1+1)] for y in range(len_str2+1)]                  
        for y in range(len_str2+1):
            for x in range(len_str1+1):
                if y == 0:
                    result_matrix[y][x] = x 
                elif x == 0:
                    result_matrix[y][x] = y 
                elif word1[x-1] == word2[y-1]:
                    result_matrix[y][x] = result_matrix[y-1][x-1]
                else:
                    result_matrix[y][x] = 1 + min(result_matrix[y-1][x],
                                                  result_matrix[y][x-1],
                                                  result_matrix[y-1][x-1])
        return result_matrix[len_str2][len_str1]
