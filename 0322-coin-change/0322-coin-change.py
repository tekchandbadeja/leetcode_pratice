# def solve_recursion(coins,amount):
#         ### base case 
#         if amount==0:
#                 return 0
#         if amount<0:
#                 return float('inf')
        
#         #### we want minium number of coins so i am taking starting minium as highst value and update it 
#         mini=float('inf')
        
#         #### saare coins per jaana hai 
#         for i in range (len(coins)):
#                 #### yha ab me again function calling kar dunga 
                
#                 small_output=solve_recursion(coins,amount-coins[i])
                
#                 ### anb mai mere small_output ko check kar kar leta h 
                
#                 if small_output!=float('inf'):
                        
#                         mini=min(mini,1+small_output)
                        
#         return mini 

def solve_rec_dp(coins,amount,dp):
        
        if amount==0:
                return 0
        if amount<0:
                return float('inf')
        
        if dp[amount]!=-1:
                
                return dp[amount]
        
        mini=float('inf')
        
        for i in range (len(coins)):
                
                small_output=solve_rec_dp(coins,amount-coins[i],dp)
                
                if small_output!=float('inf'):
                        
                        mini=min(mini,1+small_output)
                        
        dp[amount]=mini
        return dp[amount]
        
        

                        
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # output=solve_recursion(coins,amount)
        # if output==float('inf'):
        #         return -1
        # return output 
        
        ### recursion se delh liya ab memo use karenge 
        
        dp=[-1 for i in range (amount+1)]
        
        ans=solve_rec_dp(coins,amount,dp)
        
        if ans==float('inf'):   #### matlab mere amount given coin se banna possible nhi hai 
                return -1
        
        return ans 
                