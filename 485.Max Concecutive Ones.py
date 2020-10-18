class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        ct = 0
        for i in nums:
            if(i==1):
                ct +=1
                l = max(l,ct)
            else:
                ct = 0
        return l