class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        part = len(s)//k + (len(s)%k>0)
        ans = ''
        for i in range(1, part+1):
            if i%2 == 1:
                ans += s[(i-1)*k:(i*k)][::-1]
            else:
                ans += s[(i-1)*k:(i*k)]
        return ans