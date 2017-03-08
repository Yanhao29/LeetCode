class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        b = []
        while(num>0):
            b.append(num % 2)
            num = num // 2
        ans = 0
        count = 0
        for x in b:
            ans += abs(x-1)*pow(2,(count))
            count += 1
        return ans