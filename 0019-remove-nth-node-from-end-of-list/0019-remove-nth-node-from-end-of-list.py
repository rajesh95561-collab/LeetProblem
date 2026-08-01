# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp != None:
            count+=1
            temp = temp.next
        if count == n:
            new_head = head.next
            del head
            return new_head
        temp = head
        stop = count-n
        flag = 1
        while flag<stop:
            temp = temp.next
            flag+=1
        temp.next = temp.next.next
        return head