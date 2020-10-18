class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if(len(matrix)==0):
            return False
        if(len(matrix[0])==0):
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = m*n - 1
        
        while start<=end:
            mid = (start+end)//2
            num = matrix[mid//n][mid%n]
            if num==target:
                return True
            elif num>target:
                end = mid-1
            else:
                start = mid+1
        
        return False
        
            