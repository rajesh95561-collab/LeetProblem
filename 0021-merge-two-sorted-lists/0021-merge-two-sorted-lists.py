class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        flag = list1
        while flag.next:
            flag = flag.next
        flag.next = list2

        box = []

        temp = list1
        while temp:
            box.append(temp.val)
            temp = temp.next

        box.sort()

        temp = list1
        index = 0
        while temp:
            temp.val = box[index]
            index += 1
            temp = temp.next

        return list1