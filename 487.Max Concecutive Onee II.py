class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = -1
        crt = 0
        l = 0
        for i in nums:
            if i==0:
                pre = crt
                crt = 0
            else:
                crt += 1
            l = max(l, pre+1+crt)
        return l