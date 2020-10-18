# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxdepth = 0
        self.leftval = root.val
        self.helper(root, 0)
        return self.leftval
        
    def helper(self, root, depth):
        if root == None:
            return 
        if depth>self.maxdepth:
            self.maxdepth = depth
            self.leftval = root.val
            
        self.helper(root.left, depth+1) 
        self.helper(root.right, depth+1)