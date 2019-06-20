# Question : 21
# Difficulty : Easy
# Time : O(len(l1) + len(l2))
# Space : O(len(l1) + len(l2))
# Runtime : 50 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_list = []
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    new_list.append(l1.val)
                    l1 = l1.next
                else:
                    new_list.append(l2.val)
                    l2 = l2.next
            elif l1:
                new_list.append(l1.val)
                l1 = l1.next
            elif l2:
                new_list.append(l2.val)
                l2 = l2.next
        
        return new_list
