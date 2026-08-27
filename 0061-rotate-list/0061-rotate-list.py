# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        node_count = 0
        temp = head
        while temp:
            node_count+=1
            temp = temp.next
        k = k%node_count
        if k == 0:
            return head
        ptr = node_count - k
        i = 0
        temp = head
        pre = None
        while temp and i < ptr:
            pre = temp
            temp = temp.next
            i+=1
        new_head = temp
        pre.next = None
        temp = new_head
        while temp and temp.next:
            temp = temp.next
        temp.next = head
        return new_head