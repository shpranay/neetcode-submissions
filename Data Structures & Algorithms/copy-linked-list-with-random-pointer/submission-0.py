class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return None

        # Map original node -> copied node
        oldToNew = {}

        # Step 1: Create all new nodes
        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next

        # Step 2: Connect next and random pointers
        curr = head
        while curr:
            oldToNew[curr].next = oldToNew.get(curr.next)
            oldToNew[curr].random = oldToNew.get(curr.random)
            curr = curr.next

        # Return copied head
        return oldToNew[head]