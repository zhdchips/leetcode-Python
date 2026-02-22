# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            leftMax = max(0, dfs(root.left))
            rightMax = max(0, dfs(root.right))

            nonlocal res
            res = max(res, leftMax + rightMax + root.val)

            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res
        
