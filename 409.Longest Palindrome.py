class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        uni = set(s)
        res = 0
        single = False
        for x in uni:
            res = res+s.count(x)/2
            single = (s.count(x) % 2) or single
        return res*2+single