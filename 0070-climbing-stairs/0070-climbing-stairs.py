def helper(n,dp):
        if n==1:
                return 1
        
        dp[1]=1
        dp[2]=2
        
        i=3
        while i<=n:
                dp[i]=dp[i-1]+dp[i-2]
                
                i=i+1
        return dp[n]
class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp=[0 for i in range (n+1)]
        
        
        ans=helper(n,dp)
        return ans 
        