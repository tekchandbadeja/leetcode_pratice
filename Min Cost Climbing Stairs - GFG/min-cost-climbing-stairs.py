#Back-end complete function Template for Python 3
# def solve(cost,n,dp):
#     if n==0:
#         #### means tume 0 vaale stair se chlkar aaye ho
#         return cost[0]
        
#     if n==1: 
#         ### means tumne first stair se chlna start kiya hai
        
#         return cost[1]
        
#     if dp[n]!=-1:
#         return dp[n]
        
#     dp[n]=cost[n]+min(solve(cost,n-1,dp),solve(cost,n-2,dp))
#     return dp[n]

def helper(cost,n):
    dp=[-1 for i in range (n+1)]
    
    dp[0]=cost[0]
    dp[1]=cost[1]
    
    i=2
    while i<n:
        dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        
        i=i+1
        
    return min(dp[n-1],dp[n-2])
    
class Solution:
    def minCostClimbingStairs(self, cost, n):
        #Write your code here
        
        #ans=min(solve(cost,n-1),solve(cost,n-2))
        
        #return ans 
        
        
        ####optimisation 
        # dp=[-1 for i in range (n+1)]
        # ans=min(solve(cost,n-1,dp),solve(cost,n-2,dp))
        
        # return ans 
        return helper(cost,n)
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        cost=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.minCostClimbingStairs(cost,N))
# } Driver Code Ends