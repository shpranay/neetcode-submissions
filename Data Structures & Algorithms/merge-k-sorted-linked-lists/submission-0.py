class Solution:
    def mergeKLists(self, lists):
        heap = []

        # Put the first node of every list into the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            # Add smallest node to result
            curr.next = node
            curr = curr.next

            # Add next node from the same list
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next