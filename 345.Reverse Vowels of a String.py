class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        ans = list(s)
        i = 0
        j = len(s)-1
        flag1 = False
        flag2 = False
        while i<j:
            if ans[i].lower() in 'aeiou':
                flag1 = True
            else:
                i += 1
            if ans[j].lower() in 'aeiou':
                flag2 = True
            else:
                j -= 1
            if flag1 and flag2:
                tmp = ans[i]
                ans[i] = ans[j]
                ans[j] = tmp
                i += 1
                j -= 1
                flag1, flag2 = False, False
        return ''.join(ans)