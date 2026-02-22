# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        stack.append((root, 0))
        res = []
        while stack:
            cur, flag = stack.pop()
            if not cur:
                continue

            if flag: # 处理过
                res.append(cur.val)
            else:
                stack.append((cur.right, 0))
                stack.append((cur, 1))
                stack.append((cur.left, 0))
        return res
            