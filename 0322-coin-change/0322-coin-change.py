def helper(coins,index,amount,dp):
        
        if index==0:
             if amount%(coins[index])==0:
                return amount//(coins[index])
             
             else:
                return (10**9)+7
        if dp[index][amount]!=-1:
                return dp[index][amount]
        
        
        not_pick=0+helper(coins,index-1,amount,dp)
        
        pick=(10**9)+7
        
        if coins[index]<=amount:
                pick=1+helper(coins,index,amount-coins[index],dp)
                
        dp[index][amount]= min(pick,not_pick)
        return dp[index][amount]
        
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        n=len(coins)
        
        dp=[[-1 for i in range (amount+1)] for j in range (n+1)]
        
        ans=helper(coins,n-1,amount,dp)
        
        if ans==(10**9)+7:
                return -1
        else:
                return ans 
        