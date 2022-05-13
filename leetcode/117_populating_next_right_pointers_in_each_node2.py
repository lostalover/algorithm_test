# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.root = root
        self.stack = []
        cur = self.root
        self.__set_next(cur)
        return root

    def __set_next(self, cur: Node):
        if cur is None:
            return
        if len(self.stack) != 0:
            cur.next = self.stack.pop()

        if cur.right is not None:
            self.__set_next(cur.right)
        if cur.left is not None:
            self.__set_next(cur.left)

        self.stack.append(cur)


n7 = Node(val=7, left=None, right=None)
n5 = Node(val=5, left=None, right=None)
n4 = Node(val=4, left=None, right=None)
n3 = Node(val=3, left=None, right=n7)
n2 = Node(val=2, left=n4, right=n5)
n1 = Node(val=1, left=n2, right=n3)
temp = Solution().connect(n1)
print(temp)