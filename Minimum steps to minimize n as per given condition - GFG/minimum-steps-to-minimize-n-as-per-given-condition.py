#User function Template for python3
def solve(n,dp):
    
    if n==1:
        return 0
        
    ans1=float('inf')
    if n%3==0:
        if dp[n//3]==-1:
            ans1=solve(n//3,dp)
            dp[n//3]=ans1
        else:
            ans1=dp[n//3]
            
    ans2=float('inf')
    if n%2==0:
        if dp[n//2]==-1:
            ans2=solve(n//2,dp)
            dp[n//2]=ans2
        else:
            ans2=dp[n//2]
            
    if dp[n-1]==-1:
        ans3=solve(n-1,dp)
        dp[n-1]=ans3
    else:
        ans3=dp[n-1]
    
    ans=1+min(ans1,ans2,ans3)
    return ans 
class Solution:
	def minSteps(self, N):
		# code here
		dp=[-1 for i in range (N+1)]
		
		ans=solve(N,dp)
		return ans 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.minSteps(N)
		print(ans)

# } Driver Code Ends