# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(root,sub):
            q_r = collections.deque([])
            q_s = collections.deque([])
            q_r.append(root)
            q_s.append(sub)
            while q_r and q_s:
                x = q_r.popleft()
                y = q_s.popleft()
                if x.val != y.val:
                    return False
                if x.left and y.left:
                    q_r.append(x.left)
                    q_s.append(y.left)
                elif x.left or y.left:
                    return False
                if x.right and y.right:
                    q_r.append(x.right)
                    q_s.append(y.right)
                elif x.right or y.right:
                    return False
            return len(q_r) == len(q_s)


        def tree(r,s):
            if r == None:
                return False
            if s == None:
                return True
            if r.val == s.val and check(r,s):
                return True
            return tree(r.left,s) or tree(r.right,s)

        return tree(root,subRoot)
    