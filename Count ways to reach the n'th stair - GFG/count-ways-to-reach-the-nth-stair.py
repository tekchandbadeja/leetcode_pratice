#User function Template for python3
def helper(n,dp):
    m=10**9+7
    if n<=1:
        return 1
        
    dp[1]=1
    dp[2]=2
    
    i=3
    while i<=n:
        dp[i]=dp[i-1]+dp[i-2]
        i=i+1
        
    return dp[n]%m
class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        
        # code here
        dp=[0 for i in range (n+1)]
        
        ans=helper(n,dp)
        return ans 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))

# } Driver Code Ends