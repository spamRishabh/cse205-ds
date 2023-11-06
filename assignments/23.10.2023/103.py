# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = [root]
        left_to_right = True  # Flag to track traversal direction

        while queue:
            level_vals = []
            next_level = []

            for node in queue:
                if left_to_right:
                    level_vals.append(node.val)
                else:
                    level_vals.insert(0, node.val)

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            result.append(level_vals)
            queue = next_level
            left_to_right = not left_to_right

        return result
