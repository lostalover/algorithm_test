from typing import Optional


MAX_VAL = 101
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        self.result = ListNode()
        cur = self.result
        while list1 is not None or list2 is not None:
            l1_val = list1.val if list1 is not None else MAX_VAL
            l2_val = list2.val if list2 is not None else MAX_VAL
            if l1_val > l2_val:
                temp = ListNode(l2_val)
                cur.next = temp
                cur = cur.next
                list2 = list2.next
            else:
                temp = ListNode(l1_val)
                cur.next = temp
                cur = cur.next
                list1 = list1.next
        return self.result.next

l3 = ListNode(val=4)
l2 = ListNode(val=2, next=l3)
l1 = ListNode(val=1, next=l2)
m3 = ListNode(val=4)
m2 = ListNode(val=3, next=m3)
m1 = ListNode(val=1, next=m2)
Solution().mergeTwoLists(l1, m1)
