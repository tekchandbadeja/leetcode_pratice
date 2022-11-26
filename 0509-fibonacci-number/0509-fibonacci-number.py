def fib_helper(n,dp):
        if n==0 or n==1:
                return n
        if dp[n]!=-1:
                return dp[n]
        dp[n]=fib_helper(n-1,dp)+fib_helper(n-2,dp)
        return dp[n]
class Solution:
    def fib(self, n: int) -> int:
        dp=[-1 for i in range (n+1)]
        ans=fib_helper(n,dp)
        return ans 
        