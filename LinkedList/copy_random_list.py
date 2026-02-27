"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from node import Node


class Solution(object):
    copy_nodes = {}

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        node = head
        if node not in self.copy_nodes:
            copy_node = Node(node.val)
            self.copy_nodes[node] = copy_node
            copy_node.next = self.copyRandomList(node.next)
            copy_node.random = self.copyRandomList(node.random)

        return self.copy_nodes[node]
