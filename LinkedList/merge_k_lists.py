# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heapify, heappop, heappush
from typing import List, Optional
from LinkedList.list_node import ListNode

ListNode.__lt__ = lambda a, b: a.val < b.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        h = [head for head in lists if head]
        heapify(h)

        while h:
            node = heappop(h)
            if node.next:
                heappush(h, node.next)
            curr.next = node
            curr = curr.next

        return dummy.next
