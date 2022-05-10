from typing import Optional


class MyuListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = None

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.head = head
        self.tail = self.__create_double_linked_list()
        cur = self.tail
        for i in range(n-1):
            cur = cur.prev
        self.__remove_node(cur)
        return self.head
    
    def __create_double_linked_list(self):
        cur = self.head.next
        prev = self.head
        while cur is not None:
            cur.prev = prev
            prev = cur
            cur = cur.next
        return prev

    def __remove_node(self, node:ListNode):
        prev = node.prev
        next = node.next
        if prev is not None and prev.next is not None:
            prev.next = next
        if next is not None and next.prev is not None:
            next.prev = prev
        del node

# l5 = ListNode(val=5)
# l4 = ListNode(val=4, next=l5)
# l3 = ListNode(val=3, next=l4)
# l2 = ListNode(val=2, next=l3)
# l1 = ListNode(val=1, next=l2)
# Solution().removeNthFromEnd(l1, 2)

# l2 = ListNode(val=2)
# l1 = ListNode(val=1, next=l2)
# Solution().removeNthFromEnd(l1, 1)

l1 = ListNode(val=1)
Solution().removeNthFromEnd(l1, 1)
