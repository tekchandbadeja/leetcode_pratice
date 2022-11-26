# def f(height,idx,dp):
#     if idx==0:
#         return 0
        
#     if dp[idx]!=-1:
#         return dp[idx]
        
#     left=f(height,idx-1,dp)+abs(height[idx]-height[idx-1])
    
#     right=float('inf')
    
#     if idx>1:
#         right=f(height,idx-2,dp)+abs(height[idx]-height[idx-2])
        
#     dp[idx]= min(left,right)
#     return dp[idx]
    
 

    
class Solution:
    def minimumEnergy(self, height, n):
        dp=[-1 for i in range (n+1)]
        # return f(height,n-1,dp)
        
        dp[0]=0
        i=1
        while i<=n-1:
            
            fs=dp[i-1]+abs(height[i]-height[i-1])
            ss=float('inf')
            if i>1:
                ss=dp[i-2]+abs(height[i]-height[i-2])
            dp[i]=min(fs,ss)
            i+=1
        return dp[n-1]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        height = list(map(int, input().split()))
        ob = Solution()
        print(ob.minimumEnergy(height, n))
# } Driver Code Ends