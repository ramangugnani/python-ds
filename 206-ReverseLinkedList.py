# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        temp = None
        while head is not None:
            temp = head
            head = head.next
            temp.next = new_head
            new_head = temp

        return new_head

    def printList(self,head: ListNode):
        while head is not None:
            print(head.val)
            head = head.next

node6 = ListNode(6)
node5 = ListNode(5,node6)
node4 = ListNode(4,node5)
node3 = ListNode(3,node4)
node2 = ListNode(2,node3)
node1 = ListNode(1,node2)

sol = Solution()
print("Actual List")
sol.printList(node1)
new_root = sol.reverseList(node1)
print("Reverse List")
sol.printList(new_root)
