# Question : 6
# Difficulty : Medium
# Time : O(n)
# Space : O(1)
# Runtime : 70 ms

class Solution(object):
    def __init__(self):
        pass

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        row = 0
        rows = numRows - 1

        length = len(s)

        toRet = ""

        if numRows == 1:
            return s

        while row <= rows:
            index=row
            dif = rows - row
            zigLength = numRows + numRows - 2
            if (row==0 or row==rows):
                #do simple addition (no middle number)
                #print "row 0 or last row"
                while( index < length ):
                    toRet += s[index]
                    index += zigLength

            else:
                #do harder addition (middle number needed)
                while ( index < length ):
                    toRet += s[index]
                    if ( index+(2*dif) < length ):
                        toRet += s[index+(2*dif)]
                    index += zigLength
            row+=1

        return toRet
