# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head):
        # ---- Phase 1: find the middle (fast/slow) ----
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # ---- Phase 2: reverse the second half ----
        second = slow.next
        slow.next = None          # CUT the list into two halves
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # prev is now the head of the reversed second half

        # ---- Phase 3: merge the two halves alternately ----
        first, second = head, prev
        while second:
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first, second = nxt1, nxt2    