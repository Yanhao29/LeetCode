# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if(len(nums)==0):
            return []
        elif(len(nums)==1):
            root = TreeNode(nums[0])
            return root
        elif(len(nums)==2):
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            return root
        elif(len(nums)==3):
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            root.right = TreeNode(nums[2])
            return root
        else:
            root = TreeNode(nums[len(nums)/2])
            root.left = self.sortedArrayToBST(nums[0:len(nums)/2])
            root.right = self.sortedArrayToBST(nums[(len(nums)/2+1):])
            return root
            

# class Solution:
#     # @param num, a list of integers
#     # @return a tree node
#     # 12:37
#     def sortedArrayToBST(self, num):
#         if not num:
#             return None

#         mid = len(num) // 2

#         root = TreeNode(num[mid])
#         root.left = self.sortedArrayToBST(num[:mid])
#         root.right = self.sortedArrayToBST(num[mid+1:])

#         return root