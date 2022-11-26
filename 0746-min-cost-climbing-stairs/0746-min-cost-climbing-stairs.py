#def solve(cost,i,dp):
        
#         if i==len(cost)-1 or i==len(cost)-2:    ### bhai mai 1 step jump kar skta hu ya do ab yadi cost me 1 elemnt ya do bache hai to mai puncgh jaunga na usko leke 
#                 return cost[i]
#         if dp[i]!=-1:
#                 return dp[i]
#         ans1=solve(cost,i+1,dp)
#         ans2=solve(cost,i+2,dp)
#         dp[i]=cost[i]+min(ans1,ans2)
        
#         return dp[i]
def solve(cost,n,dp):
        if n==0 or n==1:
                return cost[n]
        
        if dp[n]!=-1:
                return dp[n]
        
        dp[n]=min(solve(cost,n-1,dp),solve(cost,n-2,dp))+cost[n]
        return dp[n]
                
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        
        dp=[-1 for i in range (n+1)]
        
        one=solve(cost,n-1,dp)
        
        two=solve(cost,n-2,dp)
        return min(one,two)
        
        
#         n=len(cost)
        
#         if n==2:
#                 return min(cost)
#         dp=[-1 for i in range (n+1)]
#         output1=solve(cost,0,dp)          ##3 mai 0 se start kar skta hu 
#         output2=solve(cost,1,dp)    ### mai 1 se start kar skta hu 
#          ###3 bhai mere ko 0 index se start ho ya 1 index dono me se minium chiyeee esliye finally minium liya 
#         return  min(output1,output2)


