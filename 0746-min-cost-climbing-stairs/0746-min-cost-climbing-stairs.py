def solve(cost,i,dp):
        
        if i==len(cost)-1 or i==len(cost)-2:    ### bhai mai 1 step jump kar skta hu ya do ab yadi cost me 1 elemnt ya do bache hai to mai puncgh jaunga na usko leke 
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
        output1=solve(cost,0,dp)          ##3 mai 0 se start kar skta hu 
        output2=solve(cost,1,dp)    ### mai 1 se start kar skta hu 
         ###3 bhai mere ko 0 index se start ho ya 1 index dono me se minium chiyeee esliye finally minium liya 
        return  min(output1,output2)
