from list_node import ListNode


class Solution(object):
    def isPalindrome(self, head: ListNode) -> bool:
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values == values[::-1]


