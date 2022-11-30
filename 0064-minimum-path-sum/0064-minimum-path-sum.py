def helper_memo(grid,row,col,dp):
        
        if row==0 and col==0:
                return grid[row][col]
        
        if row<0 or col<0:
                
                return float('inf')
        if dp[row][col]!=-1:
                return dp[row][col]
        
        up=helper_memo(grid,row-1,col,dp)+grid[row][col]
        
        left=helper_memo(grid,row,col-1,dp)+grid[row][col]
        
        dp[row][col]=min(up,left)
        
        return dp[row][col]
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m=len(grid)
        n=len(grid[0])
        
        dp=[[-1 for i in range (n+1)] for j in range (m+1)]
        
        ans=helper_memo(grid,m-1,n-1,dp)
        return ans 
        
        
        
# '''why we not ollow the greedy path :(may be question can arise)

#          see example 1 [[1,3,1],[1,5,1],[4,2,1]]
#                 at point (0,0) if greedy there than = 1+1+4+2+1=9 because it will take best minium at that point 
#                 but answer is =1+3+1+1+1
#                 so greedy will not work due to uniformity 
                
                
#  so i have to try all the paths , only that i can know the minimum path sum ,so we have to use RECURSION '''


## bina dp ke 

'''def helper(grid,row,col):
        ### if i reached to top left point 
        if row==0 and col==0:
                return grid[row][col]
        
        #### if i go outside from the grid 
        
        if row<0 or col<0:
                return float('inf')
        
        up=grid[row][col]+helper(grid,row-1,col)
        left=grid[row][col]+helper(grid,row,col-1)
        
        return min(up,left)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m=len(grid)
        n=len(grid[0])
        
        ans=helper(grid,m-1,n-1)
        return ans '''

        
        