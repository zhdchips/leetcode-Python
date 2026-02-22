# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def depth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            leftDepth = depth(root.left)
            rightDepth = depth(root.right)
            nonlocal res
            res = max(res, leftDepth + rightDepth + 1)

            return max(leftDepth, rightDepth) + 1
        
        depth(root)

        return res - 1
