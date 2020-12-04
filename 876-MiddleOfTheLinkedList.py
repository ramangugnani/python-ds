# https://leetcode.com/problems/middle-of-the-linked-list/

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while True:
            if fast.next is not None and fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next
            if fast.next is not None and fast.next.next is None:
                slow = slow.next
                break
            if fast.next is None:
                break
        return slow


sol = Solution()

node6 = ListNode(6)
node5 = ListNode(5,node6)
node4 = ListNode(4,node5)
node3 = ListNode(3,node4)
node2 = ListNode(2,node3)
node1 = ListNode(1)

newNode = sol.middleNode(node1)

print(newNode.val)

