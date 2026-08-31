# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:        
        if not head or not head.next:
            return
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second_head = slow.next
    # 2. Sever the link between 6 and 8
        slow.next = None
        prev = None
        while second_head:
            nxt = second_head.next
            second_head.next = prev
            prev = second_head
            second_head = nxt

        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2