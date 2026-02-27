from list_node import ListNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(-1)
        temp = head
        forward = 0

        while l1 and l2:
            curr = l1.val + l2.val + forward
            if curr >= 10:
                forward = 1
                curr = curr - 10
            else:
                forward = 0
            temp.next = ListNode(curr)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            curr = l1.val + forward
            if curr >= 10:
                forward = 1
                curr = curr - 10
            else:
                forward = 0
            temp.next = ListNode(curr)
            temp = temp.next
            l1 = l1.next

        while l2:
            curr = l2.val + forward
            if curr >= 10:
                forward = 1
                curr = curr - 10
            else:
                forward = 0
            temp.next = ListNode(curr)
            temp = temp.next
            l2 = l2.next

        if forward:
            temp.next = ListNode(forward)

        return head.next