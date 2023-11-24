# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from pyparsing import Optional
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node=root
        while(node):
            if node.val==val:
                return node
            if node.val<val:
                node=node.right
            else:
                node=node.left
        return None