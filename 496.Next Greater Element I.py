class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [-1]*len(findNums)
        for i in range(0,len(findNums)):
            if findNums[i]<max(nums[nums.index(findNums[i]):]):
                ans[i] = next(x for x in nums[nums.index(findNums[i]):] if x > findNums[i])
        return ans
            
        # d = {}
        # st = []
        # ans = []
        
        # for x in nums:
        #     while len(st) and st[-1] < x:
        #         d[st.pop()] = x
        #     st.append(x)

        # for x in findNums:
        #     ans.append(d.get(x, -1))
            
        # return ans