class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            curr = prev
            for _ in range(k):
                curr = curr.next
                if not curr:
                    return dummy.next

            group_next = curr.next
            curr = prev.next
            prev_node = group_next

            while curr != group_next:
                next_node = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = next_node

            old_first = prev.next
            prev.next = prev_node
            prev = old_first