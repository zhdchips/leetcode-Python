# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum1(self, root: Optional[TreeNode], targetSum: int) -> int:
        def rootSum(root: Optional[TreeNode], targetSum: int) -> int:
            if not root:
                return 0

            cur = 0
            if root.val == targetSum:
                cur += 1
            
            return rootSum(root.left, targetSum - root.val) + rootSum(root.right, targetSum - root.val) + cur

        if not root:
            return 0

        return rootSum(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_map = {}
        prefix_map[0] = 1
        res = 0
        
        def dfs(root: Optional[TreeNode], targetSum: int, sum: int):
            if not root:
                return
            
            sum += root.val
            nonlocal res
            res += prefix_map.get(sum - targetSum, 0)

            prefix_map[sum] = prefix_map.get(sum, 0) + 1
            dfs(root.left, targetSum, sum)
            dfs(root.right, targetSum, sum)
            prefix_map[sum] = prefix_map.get(sum) - 1
        
        dfs(root, targetSum, 0)

        return res

