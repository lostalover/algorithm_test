from typing import Optional, Sized


class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Solution:
    head = ListNode()
    tail = ListNode()
    size = int()

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        self.head = head
        self.__create_double_list_node()
        k = k % self.size
        for i in range(k):
            value = self.__pop_back()
            self.__push(value)
        return self.head
    
    def __create_double_list_node(self):
        self.size = 1
        cur = self.head.next
        prev = self.head
        while True:
            cur.prev = prev
            prev = cur
            cur = cur.next
            self.size += 1
            if cur is None:
                self.tail = prev
                break

    def __pop_back(self):
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return temp.val

    def __push(self, value: int):
        temp = ListNode(val=value, next=self.head)
        self.head.prev = temp
        self.head = temp


if __name__ == "__main__":
    t4 = ListNode(val=5)
    t3 = ListNode(val=4, next=t4)
    t2 = ListNode(val=3, next=t3)
    t1 = ListNode(val=2, next=t2)
    t0 = ListNode(val=1, next=t1)
    l1 = t0

    Solution().rotateRight(l1, 7)

    # t4 = ListNode(val=5)
    # t3 = ListNode(val=4, next=t4)
    # t2 = ListNode(val=3, next=t3)
    # t1 = ListNode(val=2, next=t2)
    # t0 = ListNode(val=1, next=t1)
    # l1 = t0

    # Solution().rotateRight(ListNode(), 2)