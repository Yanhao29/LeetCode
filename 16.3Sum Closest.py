class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                cur = nums[i]+nums[j]+nums[k]
                if cur == target:
                    return cur
                if abs(cur-target)<abs(ans-target):
                    ans = cur
                if cur<target:
                    j += 1
                elif cur>target:
                    k -= 1
        return ans
        
        
        # ans = 0
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             cur = nums[i]+nums[j]+nums[k]
        #             if i==0 and j==1 and k==2:
        #                 ans = cur
        #             else:
        #                 if abs(cur-target)<abs(ans-target):
        #                     ans = cur
        # return ans