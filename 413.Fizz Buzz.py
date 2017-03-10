class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(1,n+1):
            if((i % 3 == 0) & (i % 5 != 0)):
                ans.append("Fizz")
            elif((i % 3 != 0) & (i % 5 == 0)):
                ans.append("Buzz")
            elif((i % 3 == 0) & (i % 5 == 0)):
                ans.append("FizzBuzz")
            else:
                ans.append(str(i))
        return ans
        
    # def fizzBuzz(self, n):
    #     return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]