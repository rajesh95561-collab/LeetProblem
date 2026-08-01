# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        flag = list2
        while flag and flag.next:
            flag = flag.next
            a_p = list1
            b_p = list1
        for _ in range(a-1):
            a_p = a_p.next
        for _ in range(b):
            b_p = b_p.next
        a_p.next = list2
        flag.next = b_p.next
        return list1
        