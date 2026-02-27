# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from list_node import ListNode

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        stack = []
        dummy = ListNode(-1)
        prev = dummy
        while head:
            stack.append(head)
            head = head.next
            if len(stack) == k:
                while stack:
                    node = stack.pop()
                    prev.next = node
                    prev = node
                prev.next = head

        return dummy.next
