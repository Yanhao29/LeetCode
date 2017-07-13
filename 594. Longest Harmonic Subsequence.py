
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        ans = 0
        for x in count:
            if x+1 in count:
                ans = max(ans, count[x] + count[x+1])
        return ans
#         if(len(nums)==0):
#             return 0
#         else:
#             dic = {}
#             for i in range(len(nums)):
#                 if nums[i] in dic:
#                     dic[nums[i]] = dic[nums[i]]+1
#                 else:
#                     dic[nums[i]] = 1

#             l = 0
#             for key in dic.keys():
#                 if(key+1 in dic.keys()):
#                     l = max([l, dic[key]+dic[key+1]])
#             return l