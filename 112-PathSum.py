# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if self.recursion(root,sum,0):
            return True
        else:
            return False

    def recursion(self,root: TreeNode, sum:int, till_now_sum:int) -> bool:
        if root is None:
            return None
        else:
            #print(str(sum)+"-->"+str(root.val)+"+"+str(till_now_sum))
            if root.left is None and root.right is None and sum == root.val + till_now_sum:
                #print(root.val)
                return True

            if self.recursion(root.left, sum, till_now_sum + root.val):
                return True

            if self.recursion(root.right, sum, till_now_sum + root.val):
                return True

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

print(sol.hasPathSum(node1, 22))
