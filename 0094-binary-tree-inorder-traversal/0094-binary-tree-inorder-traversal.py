# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def visit(temp,result):
            if temp == None:
                return
            visit(temp.left,result)
            result.append(temp.val)
            visit(temp.right,result)
        visit(root,result)
        return result