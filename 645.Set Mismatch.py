class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ct = [0]*len(nums)
        for i in xrange(len(nums)):
            ct[nums[i]-1] += 1
            
        return [ct.index(2)+1, ct.index(0)+1]