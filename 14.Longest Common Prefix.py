class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ''
        
        prefix = ''
        for i in range(len(strs)):
            if i==0:
                prefix = strs[0]
            else:
                j = 0
                while j<len(prefix) and j<len(strs[i]):
                    if(strs[i][j]==prefix[j]):
                        j += 1
                    else:
                        break
                prefix = prefix[:j]
        return prefix
        