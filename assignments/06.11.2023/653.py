# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inOrderTraversal(node, elements):
            if not node:
                return
            inOrderTraversal(node.left, elements)
            elements.append(node.val)
            inOrderTraversal(node.right, elements)

        elements = []
        inOrderTraversal(root, elements)

        # Use two pointers to find if there is a pair of elements adding up to k.
        left, right = 0, len(elements) - 1
        while left < right:
            current_sum = elements[left] + elements[right]
            if current_sum == k:
                return True
            elif current_sum < k:
                left += 1
            else:
                right -= 1

        return False