#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minimizeSum(self, n, triangle):
        # Code here
        
        dp=[[-1 for i in range (n)] for j in range (n)]
        
        for j in range (n):
            
            dp[n-1][j]=triangle[n-1][j]
            
        for i in range (n-2,-1,-1):
            
            for j in range (i,-1,-1):
                
                down=triangle[i][j]+dp[i+1][j]
                
                digonal=triangle[i][j]+dp[i+1][j+1]
                
                dp[i][j]=min(down,digonal)
                
        return dp[0][0]
        
        # front=[0]*n
        # curr=[0]*n
        
        # for j in range (n):
        #     front[j]=triangle[n-1][j]
            
        # for i in range (n-2,-1,-1):
            
        #     for j in range (i,-1,-1):
                
        #         down=triangle[i][j]+front[j]
                
        #         down_digonal=triangle[i][j]+front[j+1]
                
        #         curr[j]=min(down,down_digonal)
                
        #     front=curr
        # return front[0]
                

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        triangle = [list(map(int, input().split())) for _ in range(n)]
        ob = Solution()
        res = ob.minimizeSum(n, triangle)
        print(res)
# } Driver Code Ends