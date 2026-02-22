# Definition for a binary tree node.
import re
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if not node1 and not node2:
                return True
            if node1 and not node2:
                return False
            if not node1 and node2:
                return False
                return False
            if node1.val != node2.val:
                return False
            return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
        
        return dfs(root, root)
        

