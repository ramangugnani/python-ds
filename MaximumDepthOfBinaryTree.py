# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return 1 + max(left,right)


sol = Solution()
myroot1 = TreeNode(1)
myroot = TreeNode(0,myroot1)
print(sol.maxDepth(myroot))