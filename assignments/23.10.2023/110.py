# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkBalance(node):
            if not node:
                return (True, 0)
            
            left_balance, left_height = checkBalance(node.left)
            right_balance, right_height = checkBalance(node.right)
            
            if not left_balance or not right_balance or abs(left_height - right_height) > 1:
                return (False, 0)
            
            return (True, max(left_height, right_height) + 1)
        
        balanced, _ = checkBalance(root)
        return balanced