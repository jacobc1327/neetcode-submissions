# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = l1
        curr2 = l2
        dig1 = 0
        dig2 = 0
        num1 = 0
        num2 = 0
        while curr1:
            num1 += (curr1.val)* (10**dig1)
            dig1+=1
            curr1 = curr1.next

        while curr2:
            num2 += (curr2.val)* (10**dig2)
            dig2+=1
            curr2 = curr2.next
        finall = str(num1 + num2)
        final = finall[::-1]

        dummy = ListNode()
        current = dummy
        for char in final:
            current.next = ListNode(int(char))
            current = current.next
        return dummy.next

