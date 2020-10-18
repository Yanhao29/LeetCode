class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[0]==0:
            return [1]
        else:
            cur = len(digits)-1
            if digits[cur]!=9:
                digits[cur] += 1
                return digits
            else:
                if cur==0:
                    return [1,0]
                else:
                    ans = self.plusOne(digits[:cur])
                    ans.append(0)
                    return ans                