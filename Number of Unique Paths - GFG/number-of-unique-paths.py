#User function Template for python3

   
class Solution:
    #Function to find total number of unique paths.
    def NumberOfPaths(self,a, b):
        #code here
        
        dp=[[-1 for i in range (b)] for j in range (a)]
        
        for i in range (a):
            for j in range (b):
                
                if i==0 and j==0:
                    dp[i][j]=1
                    
                else:
                    up=0
                    left=0
                    if i>0:
                        up=dp[i-1][j]
                        
                    if j>0:
                        left=dp[i][j-1]
                        
                    dp[i][j]=up+left
        return dp[a-1][b-1]
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a_b = [int(x) for x in input().strip().split()]
        a = a_b[0]
        b = a_b[1]
        ob = Solution()
        print(ob.NumberOfPaths(a, b))

# } Driver Code Ends