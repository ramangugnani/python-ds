# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode(0)
        itr = l
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                l.next = l1
                l1 = l1.next
                l = l.next
            else:
                l.next = l2
                l2 = l2.next
                l = l.next

        while l1 is not None:
            l.next = l1
            l1 = l1.next
            l = l.next

        while l2 is not None:
            l.next = l2
            l2 = l2.next
            l = l.next

        return itr.next

    def printList(self, head : ListNode):
        while head is not None:
            print(head.val)
            head = head.next


sol = Solution()
node7 = ListNode(3)
node6 = ListNode(2,node7)
node5 = ListNode(1,node6)

node4 = ListNode(5)
node3 = ListNode(4,node4)
node2 = ListNode(3,node3)
node1 = ListNode(1,node2)

print("===1===")
sol.printList(node1)
print("===2===")
sol.printList(node5)
node = sol.mergeTwoLists(node1,node5)
print("===F===")
sol.printList(node)