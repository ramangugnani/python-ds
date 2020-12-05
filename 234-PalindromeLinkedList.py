# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True

        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next


        print(slow.val)
        # odd case
        if fast is not None:
            newNode = ListNode(slow.val)
            newNode.next = slow.next
            slow.next = None
            later = newNode
            initial = head
        else:
            initial = head
            later = slow

        return True

node6 = ListNode(1)
node5 = ListNode(2,node6)
node4 = ListNode(3,node5)
node3 = ListNode(3,node4)
node2 = ListNode(2,node3)
node1 = ListNode(1,node2)

sol = Solution()
print(sol.isPalindrome(node1))