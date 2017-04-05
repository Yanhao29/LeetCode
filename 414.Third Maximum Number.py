class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_r = set(nums)
        l = list(set_r)
        if(len(list(set_r))<3):
            return max(nums)
        else:
            l.remove(max(l))
            l.remove(max(l))
            return max(l)