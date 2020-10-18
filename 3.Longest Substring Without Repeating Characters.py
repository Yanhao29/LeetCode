class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        
        start = 0
        longest = 0
        history = {}
        for i in range(len(s)):
            if s[i] in history and start<=history[s[i]]:
                start = history[s[i]]+1
            else:
                longest = max(longest, i-start+1)
            history[s[i]] = i
            
            # j = i
            # ct = 0
            # history = ''
            # stop = False
            # while j<=(len(s)-1) and not stop:
            #     if s[j] not in history:
            #         history += s[j]
            #         ct += 1
            #         j += 1
            #     else:
            #         stop = True
            # if ct>longest:
            #     longest = ct
                
        return longest
            