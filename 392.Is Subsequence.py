class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s)==0):
            return True
        ct = 0
        s_p = 0
        t_p = 0
        while t_p<len(t):
            if(s[s_p]==t[t_p]):
                ct += 1
                s_p += 1
            t_p += 1
            if(ct==len(s)):
                return True
        return False