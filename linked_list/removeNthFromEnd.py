# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = 0
        cur = head
        while cur:
            len += 1
            cur = cur.next
        step = len - n

        dummy = cur = ListNode()
        dummy.next = head
        for i in range(step):
            cur = cur.next
        
        cur.next = cur.next.next
        
        return dummy.next
        
    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        dummy = cur = ListNode()
        dummy.next = head
        
        while cur:
            stack.append(cur)
            cur = cur.next
        
        for i in range(n - 1):
            stack.pop()
        target = stack.pop()
        pre = stack.pop()
        pre.next = target.next

        return dummy.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = slow = fast = ListNode()
        dummy.next = head

        for i in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next
        



        