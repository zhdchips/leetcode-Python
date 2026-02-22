# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        myDeque = collections.deque()
        myDeque.append(root)
        while myDeque:
            curLayer = []
            for _ in range(len(myDeque)):
                cur = myDeque.popleft()
                curLayer.append(cur.val)
                if cur.left:
                    myDeque.append(cur.left)
                if cur.right:
                    myDeque.append(cur.right)
            res.append(curLayer)
        return res
