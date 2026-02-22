from ast import List, Tuple
import re
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr == arr[::-1]

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            cur, pre = head, None
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre

        def fineMidNode(head: Optional[ListNode]) -> Tuple[ListNode]:
            slow = fast = head
            pre = ListNode()
            pre.next = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                pre = pre.next
            return slow, pre

        mid, pre = fineMidNode(head)
        part2 = reverseList(mid)
        part1 = head
        while part2:
            if part1.val != part2.val:
                return False
            part1 = part1.next
            part2 = part2.next

        pre.next = reverseList(mid)

        return True

            