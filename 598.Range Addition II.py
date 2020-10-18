class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        min_a = 40000
        min_b = 40000
        if not ops:
            return m*n
        
        for i in range(len(ops)):
            min_a = min(min_a, ops[i][0])
            min_b = min(min_b, ops[i][1])
        return min_a*min_b