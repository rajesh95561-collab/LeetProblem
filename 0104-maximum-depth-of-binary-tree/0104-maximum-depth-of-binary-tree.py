# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self,node):
        if node == None:
            return 0
        lh = self.depth(node.left)
        rh = self.depth(node.right)
        return 1+max(lh,rh)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root)
        