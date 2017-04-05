class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        M = len(matrix)
        if(M == 0):
            return []
        else:
            N = len(matrix[0])
            if(N == 0):
                return []
            else:
                ans = []
                i = 0
                j = 0
                counter = 0
                up = False
                down = False
                while(counter<M*N):
                    ans.append(matrix[i][j])
                    if((i==0) and (j==0)):
                        if(N==1):
                            i = i+1
                        else:
                            j = j+1
                        down = True
                    elif(down==True and j==0 and i<M-1):
                        i = i+1
                        up = True
                        down = False
                    elif(down==True and j==0 and i==M-1):
                        j = j+1
                        up = True
                        down = False
                    elif(down==True and i==M-1):
                        j = j+1
                        up = True 
                        down = False
                    elif(up==True and i==0 and j<N-1):
                        j = j+1
                        up = False
                        down = True
                    elif(up==True and i==0 and j==N-1):
                        i = i+1
                        up = False
                        down = True
                    elif(up==True and j==N-1):
                        i = i+1
                        up = False
                        down = True
                    elif(down==True):
                        i = i+1
                        j = j-1
                    elif(up==True):
                        i = i-1
                        j = j+1
                    counter = counter+1
                return ans

# public class Solution {
#     public int[] findDiagonalOrder(int[][] matrix) {
#         if (matrix == null || matrix.length == 0) return new int[0];
#         int m = matrix.length, n = matrix[0].length;
        
#         int[] result = new int[m * n];
#         int row = 0, col = 0, d = 0;
#         int[][] dirs = {{-1, 1}, {1, -1}};
        
#         for (int i = 0; i < m * n; i++) {
#             result[i] = matrix[row][col];
#             row += dirs[d][0];
#             col += dirs[d][1];
            
#             if (row >= m) { row = m - 1; col += 2; d = 1 - d;}
#             if (col >= n) { col = n - 1; row += 2; d = 1 - d;}
#             if (row < 0)  { row = 0; d = 1 - d;}
#             if (col < 0)  { col = 0; d = 1 - d;}
#         }
        
#         return result;
#     }
# }


# def findDiagonalOrder(self, matrix):
#     m, n = len(matrix), len(matrix and matrix[0])
#     return [matrix[i][d-i]
#             for d in range(m+n-1)
#             for i in range(max(0, d-n+1), min(d+1, m))[::d%2*2-1]]

# def findDiagonalOrder(self, matrix):
#     entries = [(i+j, (j, i)[(i^j)&1], val)
#                for i, row in enumerate(matrix)
#                for j, val in enumerate(row)]
#     return [e[2] for e in sorted(entries)]