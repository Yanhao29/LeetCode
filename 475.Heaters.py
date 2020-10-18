class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses = sorted(houses)
        heaters = sorted(heaters)+[10**10]
        
        minR = 0
        c = 0
        for h in houses:
            while h>((heaters[c]+heaters[c+1])*1.0/2):
                c +=1
            minR = max(minR, abs(heaters[c]-h))
        return minR
        
        # maxD = 0
        # for i in houses:
        #     minR = 10**10
        #     for j in heaters:
        #         r = abs(j-i)
        #         if r<minR:
        #             minR = r
        #     if minR>maxD:
        #         maxD = minR
        # return maxD
                