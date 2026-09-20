import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        minHeap = []

        # 1. Add the first node of each linked list to the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node))

        dummy = ListNode(0)
        curr = dummy

        # 2. Keep taking the smallest node
        while minHeap:
            val, i, node = heapq.heappop(minHeap)

            # Attach the smallest node to our merged list
            curr.next = node
            curr = curr.next

            # Add the next node from the same linked list
            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))

        return dummy.next