import numpy as np
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = np.zeros((n,n))
        return self.helper(table,1,n)
        
    def helper(self, table, m, M):
        if m>=M or m<0 or M<=0:
            return 0 
        if table[m-1, M-1] != 0:
            return table[m-1, M-1]
        
        # ans = 0
        # for i in range(m,M+1):
        #     cur = i + max(self.helper(table, m, i-1), self.helper(table, i+1,M))
        #         f ans == 0:
        #         ans = cur
        #     else:
        #         ans = min(ans, cur)
        # table[m-1][M-1] = ans
        re = min([i + max(self.helper(table, m, i-1), self.helper(table, i+1,M)) for i in range(m,M+1)])
        table[m-1][M-1] = re
        return int(re)


# from collections import defaultdict

# class Solution(object):
#     cache = defaultdict(int)

#     def getMoneyAmount(self, r, l=0):
#         if self.cache[(r, l)]:
#             return self.cache[(r, l)]
#         if l < 0 or r <= 0 or l >= r:
#             return 0
#         re = min([max(self.getMoneyAmount(i-1, l) , self.getMoneyAmount(r, i+1)) + i for i in xrange(l, r+1)])
#         self.cache[(r, l)] = re
#         return re