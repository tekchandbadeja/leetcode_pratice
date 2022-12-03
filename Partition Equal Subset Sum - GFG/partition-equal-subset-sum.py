# User function Template for Python3

def helper(arr,n,target):
    
    dp=[[0 for i in range (target+1)] for i in range (n+1)]
    
    for i in range (n):
        dp[i][0]=True 
        
    if arr[0]<=target:
        dp[0][arr[0]]=True 
        
    for i in range (1,n):
        for j in range (1,target+1):
            
            not_take=dp[i-1][j]
            
            take=False 
            if arr[i]<=j:
                take=dp[i-1][j-arr[i]]
                
            dp[i][j]=take or not_take 
            
    return dp[n-1][target]

class Solution:
    def equalPartition(self, N, arr):
        # code here
        total_sum=0
        for i in range (N):
            total_sum+=arr[i]
            
        if total_sum%2!=0:
            return False 
            
        else:
            target=total_sum//2
            
            ans=helper(arr,N,target)
            return ans 


#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends