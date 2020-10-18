class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==0):
            return 0
        pre = 0
        crt = 0
        for i in nums:
            temp = crt
            crt = max(pre+i, crt)
            pre = temp
        return crt