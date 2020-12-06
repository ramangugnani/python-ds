# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        my_q = list()
        my_q.append(root)
        my_q.append(None)
        prev = None
        while len(my_q) > 0:
            element = my_q.pop(0)
            if element is None :
                if len(my_q) > 0:
                    my_q.append(None)
                    prev = None
                else:
                    break
            else:
                #print("data---->"+str(element.val))
                if prev is not None:
                    print("linking---->" + str(prev.val) + " to " + str(element.val))
                    prev.next = element
                    prev = element
                else:
                    prev = element
                    #print("assigning previous to ---->" + str(element.val))

                if element.left is not None:
                    my_q.append(element.left)
                if element.right is not None:
                    my_q.append(element.right)

        return root

    def connectNew(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        Q = deque()
        Q.append(root)

        while Q:
            size = len(Q)
            prev = None
            for i in range(size):
                node = Q.popleft()
                #print(str(node.val))
                if prev is not None:
                    prev.next = node
                    print("linking---->" + str(prev.val) + " to " + str(node.val))
                prev = node

                if node.left is not None:
                    Q.append(node.left)
                if node.right is not None:
                    Q.append(node.right)

        return root

sol = Solution()
node7 = Node(7)
node5 = Node(5)
node4 = Node(4)
node3 = Node(3,None,node7)
node2 = Node(2,node4,node5)
node1 = Node(1,node2,node3)

sol.connect(node1)
sol.connectNew(node1)

