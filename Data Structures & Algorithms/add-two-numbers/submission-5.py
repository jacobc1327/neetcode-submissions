# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0 

        while l1 or l2 or carry>0:
            if l1:
                dig1 = l1.val 
                l1 = l1.next
            else:
                dig1 = 0
            if l2:
                dig2 = l2.val
                l2 = l2.next
            else:
                dig2 = 0
            total = dig1 + dig2 + carry
            
            carry = total // 10
            remainder = total % 10

            curr.next = ListNode(remainder)  
            curr = curr.next


        return dummy.next 

