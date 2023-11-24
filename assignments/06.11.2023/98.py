# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(root, left, right):
            if not root:
                return True
            
            return (left < root.val and root.val < right) and validate(root.left, left, root.val) and validate(root.right, root.val, right)
            
            
        return validate(root, float('-inf'), float('inf'))