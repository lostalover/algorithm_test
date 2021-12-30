# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = self.__get_ListNode_number(l1)
        n2 = self.__get_ListNode_number(l2)
        result = self.__create_ListNode(n1 + n2)
        return result

    def __get_ListNode_number(self, list_node: ListNode):
        if list_node.next is not None:
            return int(f'{self.__get_ListNode_number(list_node.next)}' + f'{list_node.val}')
        else:
            return int(list_node.val)

    def __create_ListNode(self, number: int) -> ListNode:
        q = number // 10
        r = number % 10
        if q == 0:
            ln = ListNode(val=r)
            return ln
        else:
            ln = self.__create_ListNode(q)
            return ListNode(val=r, next=ln)


if __name__ == "__main__":
    t2 = ListNode(val=3)
    t1 = ListNode(val=4, next=t2)
    t0 = ListNode(val=2, next=t1)
    l1 = t0

    t2 = ListNode(val=4)
    t1 = ListNode(val=6, next=t2)
    t0 = ListNode(val=5, next=t1)
    l2 = t0

    Solution().addTwoNumbers(l1, l2)
