def helper(obstacleGrid,row,col,dp):
        
        if row==0 and col==0 and obstacleGrid[row][col]!=1:
                return 1
        
        if row<0 or col<0:
                return 0
        
        if row>=0 and col>=0 and obstacleGrid[row][col]==1:
                return 0
        
        if dp[row][col]!=-1:
                return dp[row][col]
        
        up=helper(obstacleGrid,row-1,col,dp)
        
        left=helper(obstacleGrid,row,col-1,dp)
        
        dp[row][col]=up+left
        return dp[row][col]
        
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        
        dp=[[-1 for i in range (n+1)] for j in range (m+1)]
        
        ans=helper(obstacleGrid,m-1,n-1,dp)
        
        return ans 
        