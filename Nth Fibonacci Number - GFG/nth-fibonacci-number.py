#User function Template for python3
def fib(n,dp):
    modulo=1000000007
    if n==0 or n==1:
        return n
        
    if dp[n-1]==-1:
        ans1=fib(n-1,dp)
        dp[n-1]=ans1
        
    else:
        ans1=dp[n-1]
        
    if dp[n-2]==-1:
        ans2=fib(n-2,dp)
        dp[n-2]=ans2
        
    else:
        ans2=dp[n-2]
        
    return (ans1%modulo+ans2%modulo)%modulo
class Solution:
    def nthFibonacci(self, n):
        # code here 
        
        # 
        # if n==0 or n==1:
        #     return n
            
        # sm1=self.nthFibonacci(n-1)
        # sm2=self.nthFibonacci( n-2)
        
        # return (sm1+sm2)%modulo
        
        dp=[-1 for i in range(n+1)]
        
        ans=fib(n,dp)
        
        return ans 
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.nthFibonacci(n))
# } Driver Code Ends