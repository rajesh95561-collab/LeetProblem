class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        number_list = []
        
        # Collect odd-positioned values
        temp = head
        while temp:
            number_list.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break
        
        # Collect even-positioned values
        temp = head.next
        while temp:
            number_list.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break
        
        # Rewrite values back into nodes
        temp = head
        index = 0
        while temp:
            temp.val = number_list[index]
            index += 1
            temp = temp.next
        
        return head
