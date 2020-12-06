# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# Solution can be made simpler by adding one additional node in the front
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = None
        ptr = head
        while ptr is not None:
            if val == ptr.val:
                if prev is not None:
                    prev.next = ptr.next
                else:
                    head = head.next
            else:
                prev = ptr
            ptr = ptr.next
        return head

    def printList(self, head : ListNode):
        while head is not None:
            print(head.val)
            head = head.next

sol = Solution()
node7 = ListNode(6)
node6 = ListNode(5,node7)
node5 = ListNode(4,node6)
node4 = ListNode(3,node5)
node3 = ListNode(6,node4)
node2 = ListNode(2,node3)
node1 = ListNode(1,node2)

sol.printList(node1)
print("======")
ret = sol.removeElements(node1,1)
sol.printList(ret)
