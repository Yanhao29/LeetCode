class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k:
            return '0'

        i = 0
        while k>0 and i<(len(num)-1):
            if num[i]>num[i+1]:
                num = num[0:i]+num[i+1:]
                k -=1
                i = 0
            else:
                i += 1
        num = num[:len(num)-k]
        return str(int(num))
        
            
class Solution(object):
    def removeKdigits(self, num, k):
        if len(num) == k:
            return '0'

        i = 0
        while i<len(num)-1 and k>0:
            if num[i]>num[i+1]:
                num = num[:i]+num[i+1:]
                k -= 1
                i = 0
            else:
                i += 1
        return str(int(num[:len(num)-k]))

            