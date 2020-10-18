class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int/Users/hao/Dropbox/Projects/Regression/online_resource.txt
        """
        s = cmp(x,0)
        x = str(s*x)
        y = ''
        for i in range(len(x),0,-1):
            y += x[i-1]
        ans = int(y)
        if ans < 2**31:
            return s*ans
        else:
            return 0
        
# def reverse(self, x):
#     s = cmp(x, 0)
#     r = int(`s*x`[::-1])
#     return s*r * (r < 2**31)