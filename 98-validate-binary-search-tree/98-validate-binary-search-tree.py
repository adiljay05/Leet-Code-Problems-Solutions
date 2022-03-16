# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    isBst = True
    prev = None
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            # logic
            if self.prev and self.prev.val>=root.val:
                self.isBst = False
            self.prev = root
            self.inorder(root.right)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inorder(root)
        return self.isBst