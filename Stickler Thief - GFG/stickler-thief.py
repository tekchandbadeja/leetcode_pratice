#User function Template for python3

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        
        if n==0:
            return 0
            
        
        if n==1:
            return a[0]   ### kyuki yahee maxium hoga 
            
        if n==2:
            return max(a[0],a[1])   ### dono me se jo maxium hoga na vo le lo 
            
        dp=[0]*n
        
        dp[0]=a[0]
        
        dp[1]=max(a[0],a[1])
        
        for i in range (2,n):
            
            pick=a[i]+dp[i-2]
            
            not_pick=0+dp[i-1]
            
            dp[i]=max(pick,not_pick)
            
        return dp[i]
            
        
        
        # code here


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
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends