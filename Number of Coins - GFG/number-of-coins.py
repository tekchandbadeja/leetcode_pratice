#User function Template for python3

def solve_rec(coins,M,V,dp):
    
    if V==0:
        return 0
        
    if V<0:
        return float('inf')
        
    if dp[V]!=-1:
        return dp[V]
        
    mini=float('inf')
    
    for i in range (M):
        
        small_output=solve_rec(coins,M,V-coins[i],dp)
        
        if small_output!=float('inf') :  
            
            
            mini=min(mini,1+small_output)    ### for eg 30 bnane ke liye 25 hatya to baad me usko 1 se jodkar consider 
                                         ### karna padega na ke humko value mili the 
                                         
    dp[V]=mini
    return dp[V]
        
class Solution:
	def minCoins(self, coins, M, V):
		# code here
		
		dp=[-1 for i in range (V+1)]
		
		ans=solve_rec(coins,M,V,dp)
		
		if ans==float('inf'):
		    return -1
		    
		return ans 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		v,m = input().split()
		v,m = int(v), int(m)
		coins = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minCoins(coins,m,v)
		print(ans)

# } Driver Code Ends