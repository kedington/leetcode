import pytest
from solution import Solution 

solution = Solution()

def test_strStr():
    # Test cases
    assert solution.strStr("hello", "ll") == 2, "Test Case 1 Failed"
    assert solution.strStr("bab", "a") == 1, "Test Case 1 Failed"
    assert solution.strStr("aaaaa", "bba") == -1, "Test Case 2 Failed"
    assert solution.strStr("", "") == 0, "Test Case 3 Failed"
    assert solution.strStr("abc", "") == 0, "Test Case 4 Failed"
    assert solution.strStr("", "a") == -1, "Test Case 5 Failed"
    assert solution.strStr("mississippi", "issip") == 4, "Test Case 6 Failed"
    assert solution.strStr("mississippi", "pi") == 9, "Test Case 7 Failed"
    assert solution.strStr("mississippi", "mississippi") == 0, "Test Case 8 Failed"
