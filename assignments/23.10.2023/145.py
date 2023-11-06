# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        prev = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack[-1]

            if not root.right or root.right == prev:
                result.append(root.val)
                stack.pop()
                prev = root
                root = None
            else:
                root = root.right

        return result