class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        comp = {}
        for i in range(len(nums)):
            if nums[i] in comp:
                return [comp[nums[i]], i]
            else:
                comp[target - nums[i]] = i