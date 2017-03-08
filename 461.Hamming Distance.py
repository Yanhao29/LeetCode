class Solution(object):

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        hD = 0
        while ((x>0)|(y>0)):
            if(x%2 != y%2):
                hD +=1
            x = x//2
            y = y//2
        return hD
        
    # def toBinary(self, x):
    #     b = []
    #     while(x>0):
    #         r = x % 2
    #         x = x//2
    #         b.append(r)
    #     b.reverse()
    #     return b