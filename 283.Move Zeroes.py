class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        p = 0
        while j!=len(nums)-1:
            if(nums[p]==0):
                for i in range(p+1,len(nums)):
                    nums[i-1] = nums[i]
                nums[-1] = 0
                j +=1
            else:
                p += 1
                j += 1
                    
# def moveZeroes(self, nums):
#     zero = 0  # records the position of "0"
#     for i in xrange(len(nums)):
#         if nums[i] != 0:
#             nums[i], nums[zero] = nums[zero], nums[i]
#             zero += 1