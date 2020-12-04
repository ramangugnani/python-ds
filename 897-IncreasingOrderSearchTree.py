# https://leetcode.com/problems/increasing-order-search-tree/

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.mylist = list()
        self.traverseBST(root)
        print(self.mylist)
        self.mylist = self.mylist[::-1]
        print(self.mylist)
        myroot = None
        for value in self.mylist:
            node = TreeNode(value,None,myroot)
            myroot = node
        return myroot


    def traverseBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        self.traverseBST(root.left)
        self.mylist.append(root.val)
        self.traverseBST(root.right)


    def print(self, root: TreeNode):
        if root is None:
            return
        else:
            print(root.val)
            self.print(root.left)
            self.print(root.right)


sol = Solution()
left = TreeNode(1)
right = TreeNode(7)
myroot = TreeNode(5,left,right)
sol.print(myroot)
newroot = sol.increasingBST(myroot)
sol.print(newroot)