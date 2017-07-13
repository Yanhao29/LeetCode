class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        total = left = 0
        result = len(nums) + 1
        for right, n in enumerate(nums):
            # print 'n is {}'.format(n)
            # print 'right is {}'.format(right)
            total += n
            # print 'total is {}'.format(total)
            while total >= s:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0
        # if(len(nums)==0):
        #     return 0 
        # else:
        #     ans = 0
        #     for i in range(len(nums)):
        #         c = 0
        #         j = i
        #         cans = 0
        #         while(j<len(nums)):
        #             # print 'j is {}'.format(j)
        #             c = c + nums[j]
        #             if(c<s):
        #                 if(j==len(nums)-1):
        #                     cans = 0
        #                     break
        #                 else:
        #                     j = j+1
        #                     cans = cans+1
        #             else:
        #                 cans = cans+1
        #                 break
        #         # print 'cans is {}'.format(cans)
        #         if(cans>0):
        #             if(ans==0):
        #                 ans = cans
        #             else:
        #                 ans = min(ans,cans)
        #     return ans