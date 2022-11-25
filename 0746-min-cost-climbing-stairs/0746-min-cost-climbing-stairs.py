def solve(cost,i,dp):
        
        if i==len(cost)-1 or i==len(cost)-2:
                return cost[i]
        if dp[i]!=-1:
                return dp[i]
        ans1=solve(cost,i+1,dp)
        ans2=solve(cost,i+2,dp)
        dp[i]=cost[i]+min(ans1,ans2)
        
        return dp[i]
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n=len(cost)
        
        if n==2:
                return min(cost)
        dp=[-1 for i in range (n+1)]
        output1=solve(cost,0,dp)
        output2=solve(cost,1,dp)
        
        return  min(output1,output2)
