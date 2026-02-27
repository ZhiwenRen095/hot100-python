from list_node import ListNode


class Solution(object):
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tempA, tempB = headA, headB

        while tempA != tempB:
            tempA = tempA.next if tempA else headB
            tempB = tempB.next if tempB else headA

        return tempA


