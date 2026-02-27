class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        slow = fast = head
        hasCycle = False

        # Hava a cycle?
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hasCycle = True
                break

        # No
        if not hasCycle:
            return None

        # Yes
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
