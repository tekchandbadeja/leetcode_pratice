def helper(row,col,dp):
        if row==0 and col==0:   ### means mai neeche se chla aur top point pe aagya
                return 1
        if row<0 or col<0 :    ### means grid se out ho gye 
                return 0
        if dp[row][col]!=-1:
                return dp[row][col]
        up=helper(row-1,col,dp)
        left=helper(row,col-1,dp)
        
        dp[row][col]= up+left
        return dp[row][col]
        
        
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp=[[-1 for i in range (n+1)] for j in range (m+1)]
        
        ans=helper(m-1,n-1,dp)
        return ans 
        
        
        
# time complexity : see i you are standing at any position of a grid than you have always two choices one is 
#         going up and second is going left so there are m rows and n col 
#         so TC = 2**(m*n)
        
# space complexity : its totally depend on path that you got sc in general 
#         sc: (m-1)+(n-1)

# def helper(row,col):
#         if row==0 and col==0:   ### means mai neeche se chla aur top point pe aagya
#                 return 1
#         if row<0 or col<0 :    ### means grid se out ho gye 
#                 return 0
        
#         up=helper(row-1,col)
#         left=helper(row,col-1)
        
#         return up+left

        
                
        