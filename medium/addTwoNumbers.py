# Question : 2
# Time : O(n)
# Space : O(n)
# Runtime : 100 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        carry = 0
        result = []
        while l1 or l2 or carry:
            foo = 0
            if l1:
                foo += l1.val
                l1 = l1.next
            if l2:
                foo += l2.val
                l2 = l2.next
            foo += carry
            result.append(foo % 10)
            carry = 1 if foo > 9 else 0
        return result

TestCases = [
        [2, 4, 3],
        [5, 6, 4],
        [],
        [],
        [],
        [0],
        [],
        [0],
        [0],
        [0],
        [1],
        [0],
        [1],
        [1],
        [9],
        [1],
        [9],
        [9],
        [9],
        [1, 2, 3, 4, 1],
        [9],
        [1, 0, 1],
        [1],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [1, 8],
        [0]]
