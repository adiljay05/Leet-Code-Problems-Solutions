# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,ans,root):
        if root:
            self.inorder(ans,root.left)
            ans.append(root.val)
            self.inorder(ans,root.right)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.inorder(ans,root)
        return ans
            