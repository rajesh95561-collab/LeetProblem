# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root == None:
            return result
        queue = collections.deque([])
        queue.append(root)
        while len(queue) != 0:
            temp = []
            level = len(queue)
            for _ in range(level):
                x = queue.popleft()
                temp.append(x.val)
                if x.left is not  None:
                    queue.append(x.left)
                if x.right is not None:
                    queue.append(x.right)
            result.append(temp)
        return result