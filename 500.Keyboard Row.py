class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        R1 = ['q','w','e','r','t','y','u','i','o','p']
        R2 = ['a','s','d','f','g','h','j','k','l']
        R3 = ['z','x','c','v','b','n','m']
        
        ans = []
        for word in words:
            flag1 = sum([True for c in word.lower() if c not in R1])
            flag2 = sum([True for c in word.lower() if c not in R2])
            flag3 = sum([True for c in word.lower() if c not in R3])
            if(flag1==0 or flag2==0 or flag3==0):
                ans.append(word)
                
        return ans