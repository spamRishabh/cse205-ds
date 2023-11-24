# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def addtoleft(root):
            if root.left == None :
                return root.right
            elif root.right == None:
                return root.left
            left1 = root.left
            l = left1
            right1 = root.right

            while l.right != None:
                l = l.right
            l.right = right1
            return left1

        if root and root.val == key:
            return addtoleft(root)

        root1 = root
        while (root1 != None):
            if root1.val > key:
                if root1.left != None and root1.left.val == key:
                    root1.left = addtoleft(root1.left)
                    break
                else :
                    root1 = root1.left
            elif root1.val < key:
                if root1.right != None and root1.right.val == key:
                    root1.right = addtoleft(root1.right)
                    break
                else :
                    root1 = root1.right
            
        return root
z