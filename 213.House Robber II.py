class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==0):
            return 0
        
        if(len(nums)<4):
            return max(nums)
        
        pre = 0
        crt = 0
        for i in nums[:-1]:
            temp = crt
            crt = max(pre+i, crt)
            pre = temp
            
        pre2 = 0
        crt2 = 0
        for i in nums[1:]:
            temp = crt2
            crt2 = max(pre2+i, crt2)
            pre2 = temp
        return max(crt, crt2)