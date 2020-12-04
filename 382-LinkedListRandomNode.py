# Definition for singly-linked list.

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:

    def __init__(self, head: ListNode):
        self.myhead = head
        self.start = head

    def getRandom(self) -> int:
        if self.start is None:
            self.start = self.myhead
        value = self.start.val
        self.start = self.start.next
        return value

# Your Solution object will be instantiated and called as such:

head2 = ListNode(3)
head1 = ListNode(2,head2)
head = ListNode(1,head1)
obj = Solution(head)
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())