import pytest
from solution import Solution  

solution = Solution()

def test_romanToInt():
    # Test cases
    assert solution.romanToInt("III") == 3, "Test Case 1 Failed"
    assert solution.romanToInt("IV") == 4, "Test Case 2 Failed"
    assert solution.romanToInt("IX") == 9, "Test Case 3 Failed"
    assert solution.romanToInt("LVIII") == 58, "Test Case 4 Failed"
    assert solution.romanToInt("MCMXCIV") == 1994, "Test Case 5 Failed"
    assert solution.romanToInt("MMMCMXC") == 3990, "Test Case 6 Failed"
    assert solution.romanToInt("CCLXXXI") == 281, "Test Case 7 Failed"
    assert solution.romanToInt("MDCLXVI") == 1666, "Test Case 8 Failed"
    assert solution.romanToInt("MMXXIV") == 2024, "Test Case 9 Failed"
    assert solution.romanToInt("XII") == 12, "Test Case 10 Failed"
    assert solution.romanToInt("M") == 1000, "Test Case 11 Failed"
    assert solution.romanToInt("CM") == 900, "Test Case 12 Failed"
    assert solution.romanToInt("XC") == 90, "Test Case 13 Failed"
    assert solution.romanToInt("I") == 1, "Test Case 14 Failed"
