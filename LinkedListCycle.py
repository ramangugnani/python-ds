# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


sol = Solution()

node4 = ListNode(4)
node3 = ListNode(0)
node2 = ListNode(2)
node1 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(sol.hasCycle(node1))