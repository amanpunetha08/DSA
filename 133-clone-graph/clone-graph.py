"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        c = Node(node.val)
        mapper = {node:c}
        q = deque([node])

        while q:
            node = q.popleft()
            clone = mapper[node]
            for nei in node.neighbors:
                if nei not in mapper:
                    nei_clone = Node(nei.val)
                    mapper[nei]= nei_clone
                    clone.neighbors.append(nei_clone)
                    q.append(nei)
                else:
                    clone.neighbors.append(mapper[nei])
        return c

        