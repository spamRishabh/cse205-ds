class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first = self.middle = self.last = None
        self.prev = TreeNode(-math.inf)
        self.inorder(root)
        if self.first and self.last :
            self.first.val, self.last.val = self.last.val, self.first.val
        else:
            if self.first and self.middle:
                self.first.val, self.middle.val = self.middle.val, self.first.val
        
    def inorder(self, root):
        if not root:
            return None
        self.inorder(root.left)
        
        if self.prev is not None and (root.val < self.prev.val):
            
            if self.first is None:
                self.first = self.prev
                self.middle = root
            else:
                self.last = root
                
        self.prev = root
        self.inorder(root.right)