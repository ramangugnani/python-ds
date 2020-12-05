# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Data:
    def __init__(self,dia,height):
        self.dia = dia
        self.height = height


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        data = self.calculate(root)
        return data.dia

    def calculate(self,root: TreeNode) -> Data:
        if root is None:
            return Data(0,0)
        else:
            left = self.calculate(root.left)
            right = self.calculate(root.right)
            height = 1 + max(left.height,right.height)
            dia = max(left.dia,right.dia,left.height+right.height)
            return Data(dia,height)


sol = Solution()

node9 = TreeNode(1)
node8 = TreeNode(2)
node7 = TreeNode(7)

node6 = TreeNode(4,None,node9)
node5 = TreeNode(13)
node4 = TreeNode(11,node7,node8)

node3 = TreeNode(8,node5,node6)
node2 = TreeNode(4,node4)

node1 = TreeNode(5,node2,node3)

print(sol.diameterOfBinaryTree(node1))