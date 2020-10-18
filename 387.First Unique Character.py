class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # letters='abcdefghijklmnopqrstuvwxyz'
        # ct = {}
        # for i in letters:
    
        
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
    
        # visited = []
        # ans = -1
        # for i in range(len(s)):
        #     if s[i] in visited:
        #         ct = 2
        #     else:
        #         ct = 1
        #         for j in range(i+1,len(s)):
        #             if s[j] == s[i]:
        #                 ct += 1
        #     if ct == 1:
        #         ans = i
        #         break
        #     visited.append(s[i])
        # return ans