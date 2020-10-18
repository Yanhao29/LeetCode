# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        if root is None:
            return 0
        else:
            return max(self.leftLen(root)+self.rightLen(root), 
                       self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))


    def leftLen(self, root):
        if root is None or root.left is None:
            return 0
        else:
            return 1+max(self.leftLen(root.left), self.rightLen(root.left))

    def rightLen(self, root):
        if root is None or root.right is None:
            return 0
        else:
            return 1+max(self.leftLen(root.right), self.rightLen(root.right))