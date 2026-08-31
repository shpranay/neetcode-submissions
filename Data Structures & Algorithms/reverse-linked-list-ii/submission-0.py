class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # If no reversal is needed
        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        # Move prev to the node just before 'left'
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        # Reverse the section from left to right
        curr = prev.next

        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next