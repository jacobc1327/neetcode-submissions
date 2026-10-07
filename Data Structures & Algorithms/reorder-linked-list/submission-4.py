# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head1 = head
        head2 = slow.next 
#reverse second half
        slow.next=None

        prev = None
        curr = head2

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        #head1 = head
        #prev = head2
        
        while prev:
            nxt1 = head1.next
            nxt2 = prev.next
            head1.next = prev
            prev.next = nxt1
            head1 = nxt1
            prev = nxt2
        return 
        



