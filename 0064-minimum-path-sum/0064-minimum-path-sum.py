
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m=len(grid)
        n=len(grid[0])
        
        dp=[[0 for i in range (n+1)] for j in range (m+1)]
        
        for i in range (m):
                for j in range (n):
                        if i==0 and j==0:
                                dp[i][j]=grid[i][j]
                        else:
                                up=float('inf')
                                left=float('inf')
                                if i>0:
                                        up=grid[i][j]+dp[i-1][j]
                                
                                
                                if j>0:
                                        left=grid[i][j]+dp[i][j-1]
                                
                                dp[i][j]=min(up,left)
        return dp[m-1][n-1]
        
         
        
        
        
# # '''why we not ollow the greedy path :(may be question can arise)

# #          see example 1 [[1,3,1],[1,5,1],[4,2,1]]
# #                 at point (0,0) if greedy there than = 1+1+4+2+1=9 because it will take best minium at that point 
# #                 but answer is =1+3+1+1+1
# #                 so greedy will not work due to uniformity 
                
                
# #  so i have to try all the paths , only that i can know the minimum path sum ,so we have to use RECURSION '''


# ## bina dp ke 

# #
# '''def helper(grid,row,col):
#         ### if i reached to top left point 
#         if row==0 and col==0:
#                 return grid[row][col]
        
#         #### if i go outside from the grid 
        
#         if row<0 or col<0:
#                 return float('inf')
        
#         up=grid[row][col]+helper(grid,row-1,col)
#         left=grid[row][col]+helper(grid,row,col-1)
        
#         return min(up,left)
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
        
#         m=len(grid)
#         n=len(grid[0])
        
#         ans=helper(grid,m-1,n-1)
#         return ans '''

# '''for every -function - you are calling 2 more functions( you can see that in your program) , and there are m * n calls.
# since 1 call each for a row and a col and every function -> calls 2 more functions recursively.

# There fore in total 2 calls will be called in m * n ways. (2 * 2 * 2 * 2 * 2..... m * n times)
# hence o(2^(m * n)).

# spac complexity = recursion space (O(m*n))path that we get (m-1)+(n-1)


# def helper_memo(grid,row,col,dp):
        
#         if row==0 and col==0:
#                 return grid[row][col]
        
#         if row<0 or col<0:
                
#                 return float('inf')
#         if dp[row][col]!=-1:
#                 return dp[row][col]
        
#         up=helper_memo(grid,row-1,col,dp)+grid[row][col]
        
#         left=helper_memo(grid,row,col-1,dp)+grid[row][col]
        
#         dp[row][col]=min(up,left)
        
#         return dp[row][col]
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
        
#         m=len(grid)
#         n=len(grid[0])
        
#         dp=[[-1 for i in range (n+1)] for j in range (m+1)]
        
#         ans=helper_memo(grid,m-1,n-1,dp)
#         return ans '''


        
        