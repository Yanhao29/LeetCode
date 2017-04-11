class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        if(m==0 or n==0):
            return 0
        else:
            ans = 0
            for i in xrange(0,m):
                for j in xrange(0,n):
                    if(grid[i][j]==1):
                        if(i-1<0):
                            ans = ans+1
                        elif(grid[i-1][j]==0):
                            ans = ans+1
                        if(i+1==m):
                            ans = ans+1
                        elif(grid[i+1][j]==0):
                            ans = ans+1
                        if(j-1<0):
                            ans = ans+1
                        elif(grid[i][j-1]==0):
                            ans = ans+1
                        if(j+1==n):
                            ans = ans+1
                        elif(grid[i][j+1]==0):
                            ans = ans+1
            return ans

    # def islandPerimeter(self, grid):
    #     return sum(sum(map(operator.ne, [0] + row, row + [0]))
    #            for row in grid + map(list, zip(*grid)))