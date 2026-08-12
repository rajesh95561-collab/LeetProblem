# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        height = 0
        q = deque([])
        q.append(root)
        while len(q) != 0:
            level_len = len(q)
            height+=1
            for _ in range(level_len):
                x = q.popleft()
                if x.left is not None:
                    q.append(x.left)
                if x.right is not None:
                    q.append(x.right)
        return height

        
        