class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head

        first = head
        res = second = first.next

        while first and second:
            first.next = second.next
            second.next = first
            temp = first
            first = first.next
            if first is None or first.next is None:
                break
            second = temp.next = first.next

        return res
