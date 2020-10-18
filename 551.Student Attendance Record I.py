class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cL = 0
        cA = 0
        for i in range(len(s)):
            if(s[i]=='L'):
                cL += 1
            elif(s[i]=='A'):
                cA += 1
                if(cL<3):
                    cL = 0
            else:
                if(cL<3):
                    cL = 0
        if(cL<=2 and cA<=1):
            return True
        else:
            return False