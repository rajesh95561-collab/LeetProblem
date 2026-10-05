# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def swap(self,q):
        if q is None:
            return
        left = self.swap(q.left)
        right = self.swap(q.right)
        q.left, q.right = q.right, q.left
        return q
    def check(self,p,q):
        if p == None and q == None: return True
        if p == None or q == None: return False
        if p.val != q.val: return False
        return self.check(p.left,q.left) and self.check(p.right,q.right)
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root: return True
        if (root.left and not root.right) or (root.right and not root.left): return False
        self.swap(root.right)
        return self.check(root.left,root.right)