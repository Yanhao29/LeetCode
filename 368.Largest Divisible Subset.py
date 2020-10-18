class Solution(object):
    def largestDivisibleSubset(self, nums):
        S = {-1: set()}
        for x in sorted(nums):
            # print x
            # print '**'
            # print  max((S[d] for d in S if x % d == 0), key=len)
            # print '****'
            # print x
            # print '&&&&&&&&'
            S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
            # print S[x]
            # print '~~~~~~~~'
            # print S
            # print '_________________________'
        return list(max(S.values(), key=len))