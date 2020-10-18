class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        for i in range(2,len(nums)):
            j = 0
            k = i-1
            while j<k:
                if nums[j]+nums[k]>nums[i]:
                    ans += k-j
                    k -= 1
                else:
                    j += 1
        return ans
            